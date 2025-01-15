<?php
class Mahasiswa {
    private $conn;

    // Fungsi untuk koneksi ke database
    public function connection() {
        $host = "localhost";
        $dbname = "itenas";  // Nama database yang digunakan
        $username = "root";  // Sesuaikan dengan username MySQL
        $password = "";      // Sesuaikan dengan password MySQL
        
        try {
            $this->conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            echo "Koneksi gagal: " . $e->getMessage();
        }
    }

    // Fungsi untuk membaca (READ) data dari tabel mahasiswa
    public function read() {
        $query = "SELECT * FROM mahasiswa";
        $stmt = $this->conn->prepare($query);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    // Fungsi untuk menambah (ADD) data mahasiswa
    public function add($nrp, $nama, $alamat) {
        $query = "INSERT INTO mahasiswa (nrp, nama, alamat) VALUES (:nrp, :nama, :alamat)";
        $stmt = $this->conn->prepare($query);
        $stmt->bindParam(':nrp', $nrp);
        $stmt->bindParam(':nama', $nama);
        $stmt->bindParam(':alamat', $alamat);
        return $stmt->execute();
    }

    // Fungsi untuk menghapus (DELETE) data mahasiswa
    public function delete($nrp) {
        $query = "DELETE FROM mahasiswa WHERE nrp = :nrp";
        $stmt = $this->conn->prepare($query);
        $stmt->bindParam(':nrp', $nrp);
        return $stmt->execute();
    }
}
?>