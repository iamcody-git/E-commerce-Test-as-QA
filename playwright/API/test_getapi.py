from playwright.sync_api import Playwright

def test_api_get(playwright:Playwright):
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/posts/1",
                           headers={"Accept"})

    assert response.status == 200
    json_data = response.json()
    print(json_data)
    assert json_data["id"] ==2
    request.dispose()
    print("Test succesfulyy")