"""
네이버 증권 인기 검색 종목 수집 및 Word 문서 저장 스크립트

조건:
1. Selenium으로 크롬 브라우저 실행 (예외처리 포함)
2. 네이버 증권 국내 증시 페이지 접속 (https://finance.naver.com/sise/)
3. 인기 검색 종목명 10개 수집 및 출력
4. template.docx의 {title} 부분에 제목 삽입
5. List Number 스타일로 10개 종목 추가
6. result.docx로 저장
"""

import time
import sys
from docx import Document
from docx.shared import Pt

# ── Selenium 관련 임포트 ──────────────────────────────────────────────────────
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import (
        WebDriverException,
        TimeoutException,
        NoSuchElementException,
    )
except ImportError as e:
    print(f"[오류] Selenium 라이브러리를 불러오지 못했습니다: {e}")
    print("설치 명령: pip install selenium")
    sys.exit(1)


# ── 1. 크롬 드라이버 설정 및 실행 ─────────────────────────────────────────────
def create_driver() -> webdriver.Chrome:
    """Chrome WebDriver를 생성하여 반환합니다."""
    options = Options()
    options.add_argument("--headless")           # 헤드리스 모드 (화면 없이 실행)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
    # ChromeDriver 경로가 PATH에 있다고 가정 (webdriver-manager 사용 시 자동 설정)
    try:
        driver = webdriver.Chrome(options=options)
        return driver
    except WebDriverException as e:
        raise WebDriverException(f"Chrome 드라이버 실행 실패: {e}") from e


# ── 2 & 3. 네이버 증권 접속 및 인기 검색 종목 수집 ────────────────────────────
def get_popular_stocks(driver: webdriver.Chrome) -> list[str]:
    """
    네이버 증권 국내 증시 페이지에서 인기 검색 종목 10개를 수집합니다.
    """
    url = "https://finance.naver.com/sise/"
    try:
        driver.get(url)
    except WebDriverException as e:
        raise WebDriverException(f"페이지 접속 실패 ({url}): {e}") from e

    # 페이지 로딩 대기 (최대 15초)
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "popularItemList"))
        )
    except TimeoutException:
        # ID가 다를 수 있으므로 추가 셀렉터 시도
        pass

    # 잠시 대기 (동적 콘텐츠 렌더링)
    time.sleep(2)

    stocks: list[str] = []

    # ── 셀렉터 후보 목록 (우선순위 순) ──────────────────────────────────────
    selectors = [
        # 인기 검색 종목 리스트 (공식 클래스명)
        (By.CSS_SELECTOR, "#popularItemList .item_name"),
        (By.CSS_SELECTOR, ".popular_search .item_name"),
        (By.CSS_SELECTOR, ".popular_search li a"),
        (By.CSS_SELECTOR, "#popularItemList li a"),
        (By.CSS_SELECTOR, ".rank_lst li a"),
        # 검색 순위 텍스트 노드
        (By.XPATH, '//*[@id="popularItemList"]//li//a[contains(@class,"item")]'),
        (By.XPATH, '//div[contains(@class,"popular")]//li//a'),
        (By.XPATH, '//ul[contains(@class,"rank")]//li//a'),
    ]

    for by, selector in selectors:
        try:
            elements = driver.find_elements(by, selector)
            if elements:
                stocks = [el.text.strip() for el in elements if el.text.strip()]
                if len(stocks) >= 5:          # 5개 이상이면 유효한 결과로 판단
                    print(f"[정보] 셀렉터 적용 성공: {selector}")
                    break
        except NoSuchElementException:
            continue

    # 최후 수단: 페이지 전체에서 '인기 검색' 근처 텍스트 파싱
    if len(stocks) < 5:
        try:
            page_source = driver.page_source
            from bs4 import BeautifulSoup   # beautifulsoup4가 설치된 경우만
            soup = BeautifulSoup(page_source, "html.parser")
            # 인기 검색 섹션 탐색
            for ul in soup.find_all("ul"):
                items = [li.get_text(strip=True) for li in ul.find_all("li")]
                if len(items) >= 8:
                    stocks = items
                    break
        except Exception:
            pass

    # 결과가 없으면 예외 발생
    if not stocks:
        raise RuntimeError(
            "인기 검색 종목을 찾지 못했습니다. "
            "네이버 증권 페이지 구조가 변경되었을 수 있습니다."
        )

    # 10개 제한
    return stocks[:10]


# ── 4 & 5 & 6. Word 문서 작성 및 저장 ────────────────────────────────────────
def save_to_docx(stocks: list[str], template_path: str = "template.docx",
                 output_path: str = "result.docx") -> None:
    """
    template.docx를 열어 {title}을 제목으로 교체하고,
    List Number 스타일로 종목 목록을 추가한 뒤 result.docx로 저장합니다.
    """
    title_text = "오늘의 인기 검색 종목 10개 입니다."

    try:
        doc = Document(template_path)
    except Exception as e:
        raise FileNotFoundError(f"템플릿 파일을 열 수 없습니다 ({template_path}): {e}") from e

    # 4. {title} 교체
    replaced = False
    for para in doc.paragraphs:
        if "{title}" in para.text:
            # 단순 텍스트 교체 (run 단위 처리)
            for run in para.runs:
                if "{title}" in run.text:
                    run.text = run.text.replace("{title}", title_text)
                    replaced = True
            # run이 분리된 경우를 대비한 전체 교체
            if not replaced:
                full_text = para.text
                if "{title}" in full_text:
                    # 모든 run 초기화 후 첫 run에 대체 텍스트 삽입
                    for i, run in enumerate(para.runs):
                        run.text = title_text if i == 0 else ""
                    replaced = True

    if not replaced:
        print("[경고] {title} 플레이스홀더를 찾지 못했습니다. 문서 상단에 제목을 추가합니다.")
        title_para = doc.add_paragraph(title_text)
        title_para.style = doc.styles["Heading 1"]

    # 5. List Number 스타일로 10개 종목 추가
    for stock in stocks:
        para = doc.add_paragraph(stock, style="List Number")

    # 6. result.docx 저장
    try:
        doc.save(output_path)
        print(f"\n[완료] 문서가 '{output_path}'로 저장되었습니다.")
    except Exception as e:
        raise IOError(f"문서 저장 실패 ({output_path}): {e}") from e


# ── 메인 실행부 ───────────────────────────────────────────────────────────────
def main():
    driver = None
    try:
        # 1. 크롬 드라이버 실행
        print("[1단계] Chrome 브라우저를 실행합니다...")
        driver = create_driver()
        print("        → Chrome 실행 성공")

        # 2 & 3. 네이버 증권 접속 및 인기 종목 수집
        print("\n[2단계] 네이버 증권 국내 증시 페이지에 접속합니다...")
        print("        URL: https://finance.naver.com/sise/")
        stocks = get_popular_stocks(driver)

        print("\n[3단계] 인기 검색 종목 수집 결과:")
        print("=" * 40)
        for i, stock in enumerate(stocks, start=1):
            print(f"  {i:>2}. {stock}")
        print("=" * 40)

        # 4, 5, 6. Word 문서 생성 및 저장
        print("\n[4-6단계] result.docx 문서를 생성합니다...")
        save_to_docx(stocks, template_path="template.docx", output_path="result.docx")

    except WebDriverException as e:
        print(f"\n[오류] 브라우저 오류: {e}")
        sys.exit(1)
    except TimeoutException as e:
        print(f"\n[오류] 페이지 로딩 타임아웃: {e}")
        sys.exit(1)
    except (FileNotFoundError, IOError, RuntimeError) as e:
        print(f"\n[오류] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[예상치 못한 오류] {type(e).__name__}: {e}")
        sys.exit(1)
    finally:
        # 반드시 드라이버 종료
        if driver is not None:
            driver.quit()
            print("\n[정리] Chrome 브라우저를 종료했습니다.")


if __name__ == "__main__":
    main()
