import requests
import kaggle

kaggle.api.authenticate()


def check_url(url_):
    try:
        response = requests.get(url_)
        print(response.status_code)
        if response.status_code == 200:
            data_ = response.json()['response']
            # print('data',data_)
            results = data_['results']
            # print(results)
            # return data_
            page = data_['currentPage']
            total_pages = data_['pages']
            pageSize = data_['pageSize']
            # print(page, total_pages)
            return {'results' : results , 'current_page' : page, 'total_pages' : total_pages, 'pageSize' : pageSize}

        if response.status_code != 200:
            username = input("Enter the username of the dataset: \n")
            dataset_name = input("Enter the name of the dataset: \n")
            kaggle.api.dataset_download_files(f"{username}/{dataset_name}", path='.', unzip=True)
    except ValueError as e:
        print("An error occurred: ", e)
    except AttributeError as e:
        print("An error occurred: ", e)
    except NameError as e:
        print("An error occurred: ", e)
    except BaseException as e:
        print("An error occurred: ", e)

