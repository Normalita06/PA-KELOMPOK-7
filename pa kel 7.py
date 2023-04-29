# shafa
from prettytable import PrettyTable
import mysql.connector
import pwinput
import sys
import math

class Restoran:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.saldo = 500000

    def tambah_menu(self, nama, harga):
        new_menu = Restoran(nama, harga)

        if not self.head:
            self.head = new_menu
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_menu

    def tampilan_menu(self):
        if not self.head:
            print("Tidak Ada Menu Yang Tersedia.")
        else:
            Z = 1
            current = self.head
            table = PrettyTable(["NO", "NAMA","HARGA"])
            while current:
                table.add_row([Z, current.nama, current.harga ])
                Z += 1
                current = current.next
            print (table)

    def cari_menu(self):
        if not self.head:
            print("Tidak Ada Menu Yang Tersedia")
            return
        cari = input("Masukkan nama menu yang ingin dicari: ")
        arr = self.to_array()
        n = len(arr)
        jump = int(math.sqrt(n))
        left, right = 0, 0
        while right < n and arr[right] < cari:
            left = right
            right = min(n - 1, right + jump)
        for i in range(left, right + 1):
            if arr[i] == cari:
                node = self.getindex(i)
                print(f"Menu Makanan Ditemukan pada index ke-{i+0}")
                print(f"Nama: {node.nama}")
                print(f"harga: {node.harga}")
                return

        print(f"Menu Makanan Dengan Nama {cari} Tidak Ditemukan")

    def cari1(self, index):
        return self.cari_menu(index)

    def update_menu(self, menu, nama_baru, harga_baru):
        if menu:
            menu.nama = nama_baru
            menu.harga = harga_baru
        else:
            print("Menu yang Anda cari tidak ditemukan")

    def hapus_Menu(self, index):
        if not self.head:
            print("Tidak Ada Nama Menu Yang Tersedia.")
            return
        
        if index == 1:
            self.head = self.head.next
            print("menu tersebut Berhasil Dihapus")
            return
        
        prev = None
        current = self.head
        s = 1
        while current and s != index:
            prev = current
            current = current.next
            s += 1

        if not current:
            print("Menu dengan Index tersebut Tidak Ditemukan")
            return
        
        prev.next = current.next
        current.next = None
        print("Menu Berhasil di Hapus")

    def shell_sort(self):
        s = self.get_length()
        gap = s // 2
        while gap > 0:
            for w in range(gap, s):
                temp_node = self.get_node_at_index(w)
                temp_nama = temp_node.nama
                temp_harga = temp_node.harga

                p = w
                while p >= gap and self.get_node_at_index(p - gap).nama > temp_nama:
                    node_p_gap = self.get_node_at_index(p - gap)
                    self.get_node_at_index(p).nama = node_p_gap.nama
                    self.get_node_at_index(p).harga = node_p_gap.harga
                    p -= gap
                self.get_node_at_index(p).nama = temp_nama
                self.get_node_at_index(p).harga = temp_harga
            gap //= 2

    def Cari_index(self, index):
        current = self.head
        while current is not None:
            if current.nama == index:
                return current
            current = current.next
        return None
    
    def to_array(self):
        array = []
        current_node = self.head
        while current_node is not None:
            array.append(current_node.nama)
            current_node = current_node.next
        return array
    
    def getindex(self, index):
        current_node = self.head
        current_index = 0
        while current_node is not None:
            if current_index == index:
                return current_node
            current_node = current_node.next
            current_index += 1

