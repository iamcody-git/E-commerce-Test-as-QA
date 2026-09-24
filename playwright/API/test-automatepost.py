from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Create a request context (used for API calls)
    request_context = p.request.new_context()

    # Data you want to send in the POST request
    payload = {
        "name": "cody",
        "job": "CEO"
    }

    # Make the POST request
    response = request_context.post(
        "https://reqres.in/api/users",
        data=payload
    )

    # Print status code
    print("Status Code:", response.status)

    # Print response body as JSON
    print("Response Body:", response.json())

    # Close the context when done
    request_context.dispose()