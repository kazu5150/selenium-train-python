from kuroneko_yamato import check_yamato_delivery


def main():
    contact_number = input("問い合わせ番号を入力してください：")
    result = check_yamato_delivery(contact_number)
    print(f"【{contact_number}】のお荷物：【{result}】")


if __name__ == "__main__":
    main()
    