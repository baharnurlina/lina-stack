from collections import deque

def main():
    dq = deque()

    while True:
        print("\n=== MENU DEQUE ===")
        print("1. Append (Tambah di belakang)")
        print("2. AppendLeft (Tambah di depan)")
        print("3. Pop (Hapus dari belakang)")
        print("4. PopLeft (Hapus dari depan)")
        print("5. Clear (Hapus semua data)")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            data = input("Masukkan data: ")
            dq.append(data)
            print("Deque sekarang:", dq)

        elif pilihan == "2":
            data = input("Masukkan data: ")
            dq.appendleft(data)
            print("Deque sekarang:", dq)

        elif pilihan == "3":
            if dq:
                print("Data yang di-pop:", dq.pop())
            else:
                print("Deque kosong!")
            print("Deque sekarang:", dq)

        elif pilihan == "4":
            if dq:
                print("Data yang di-pop-left:", dq.popleft())
            else:
                print("Deque kosong!")
            print("Deque sekarang:", dq)

        elif pilihan == "5":
            dq.clear()
            print("Deque berhasil di-clear!")
            print("Deque sekarang:", dq)

        elif pilihan == "6":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
