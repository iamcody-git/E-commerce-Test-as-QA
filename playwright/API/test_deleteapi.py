from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Create a request context (used for API calls)
    request_context = p.request.new_context()

    # Send DELETE request to remove a resource (user with id 2)
    response = request_context.delete("https://reqres.in/api/users/2")

    # Print status code
    print("Status Code:", response.status)

    # DELETE often returns an empty body, so check before parsing JSON
    body_text = response.text()
    print("Response Body:", body_text if body_text else "(empty response)")

    # Close the context when done
    request_context.dispose()