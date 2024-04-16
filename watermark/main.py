import argparse
import cv2
import inquirer
import numpy as np

from attack import Attack
from dct_watermark import DCT_Watermark
from dwt_watermark import DWT_Watermark


def main(args):
    global model
    img = cv2.imread(args.origin)
    wm = cv2.imread(args.watermark, cv2.IMREAD_GRAYSCALE)

    type_choices = ["DCT", "DWT"]

    # Chọn loại (type)
    type_question = [
        inquirer.List("type", message="Choice type", choices=type_choices),
    ]
    type_answer = inquirer.prompt(type_question)

    if type_answer['type'] in ["DCT", "DWT"]:
        if type_answer['type'] == 'DCT':
            model = DCT_Watermark()
        elif type_answer['type'] == 'DWT':
            model = DWT_Watermark()

        # Chọn tác vụ (embedding hoặc extracting)
        option_question = [
            inquirer.List("option", message="Choice option", choices=["embedding", "extracting"]),
        ]
        option_answer = inquirer.prompt(option_question)

        if option_answer["option"] == "embedding":
            emb_img = model.embed(img, wm)
            cv2.imwrite(args.output, emb_img)
            print("Embedded to {}".format(args.output))
        elif option_answer["option"] == 'extracting':
            signature = model.extract(img)
            cv2.imwrite(args.output, signature)
            print("Extracted to {}".format(args.output))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="compare", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--origin", default="./images/cover.jpg", help="origin image file")
    parser.add_argument("--watermark", default="./images/watermark.jpg", help="watermark image file")
    parser.add_argument("--output", default="./images/watermarked.jpg", help="embedding image file")
    args = parser.parse_args()
    main(parser.parse_args())