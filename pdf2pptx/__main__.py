from pdf2pptx.convertor import pdf2jpeg, jpeg2pptx


def main():
    import sys

    if len(sys.argv) != 3:
        print('参数错误')
        return

    images = pdf2jpeg(sys.argv[1])
    if len(images) > 0:
        jpeg2pptx(images, sys.argv[2])


if __name__ == '__main__':
    main()
