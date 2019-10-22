from python_anticaptcha import AnticaptchaClient, ImageToTextTask, NoCaptchaTaskProxylessTask

if __name__ == '__main__':
    api_key = 'ff5eaf29305bd76f3f5e87f6f51ff164'
    url = "https://i.stack.imgur.com/2zrXa.png"
    client = AnticaptchaClient(api_key)
    task = NoCaptchaTaskProxylessTask(website_url=url, website_key="")
    job = client.createTask(task)
    job.join()
    print(job.get_solution_response())

