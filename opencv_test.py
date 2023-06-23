import cv2


if __name__ == "__main__":
    # image read
    img = cv2.imread("img/Lenna.png")
    cv2.imshow("Lenna", img) # imshow(창 이름, 띄울 이미지)

    print(img.shape) # (512, 512, 3)
    # row(=세로의 길이), col(=가로의 길이), RGB 3가지 값이 있으므로 3
    # True Color. 1byte로 표현할 수 있는 칼라는 255 x 255 x 255 ?


    # waitKey 안쓰면 컴퓨터가 너무 빨라서 바로 떴다가 꺼짐
    cv2.waitKey(0) # 0 : 무한정 기다림
    cv2.destroyWindow("Lenna")