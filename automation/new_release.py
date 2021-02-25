import ciur
import requests


class Pip:
    pass

    def __contains__(self, project_module: str):
        url = f"https://pypi.org/rss/project/{ project_module.__name__ }/releases.xml"
        
        response = requests.get(url)
        return f"<title>{project_module.__version__}</title>" in response.text
        

def main():
    if ciur not in Pip():
        print(f"Create new release for ciur-{ciur.__version__}")
        exit(0)

    print(f"Maybe to create patch ciur-{ciur.__version__}+1")
    exit(1)


if __name__ == "__main__":
    main()
