from playwright.sync_api import sync_playwright

def test_auth():

    import requests
    print(requests.get("http://localhost:3000/login").status_code)  # Should print 200
        
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("http://localhost:3000/login")
        page.fill("input[name='username']", "testuser")
        page.fill("input[name='password']", "testpass")
        page.click("button[type='submit']")
        
        page.wait_for_url("**/protected")
        
        browser.close()

if __name__ == "__main__":
    test_auth()
