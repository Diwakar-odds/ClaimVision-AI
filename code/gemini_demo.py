from src.image_analyzer import analyze_image
def main():
 result = analyze_image(
    "../dataset/images/sample/case_001/img_1.jpg",
    "car"
)

print(result)
if __name__ == "__main__":
    main()