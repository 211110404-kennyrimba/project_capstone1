-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 18 Jan 2023 pada 02.24
-- Versi server: 10.4.22-MariaDB
-- Versi PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pa_web`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `daftar_menu`
--

CREATE TABLE `daftar_menu` (
  `id_menu` int(6) NOT NULL,
  `menu` varchar(255) NOT NULL,
  `harga` double(20,2) NOT NULL,
  `path` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `daftar_menu`
--

INSERT INTO `daftar_menu` (`id_menu`, `menu`, `harga`, `path`) VALUES
(1, 'Bakso', 13000.00, '../static/img/bakso.jpeg'),
(2, 'Mie ayam', 15000.00, '../static/img/mieayam.jpg'),
(4, 'Sushi', 15000.00, '../static/img/a0000370_main.png'),
(6, 'Makanan', 10000.00, '../static/img/Sate_BangDe-2021_11_16-16_33_30_3895');

-- --------------------------------------------------------

--
-- Struktur dari tabel `meja`
--

CREATE TABLE `meja` (
  `no_meja` int(2) NOT NULL,
  `keterangan` varchar(255) NOT NULL,
  `status_meja` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `meja`
--

INSERT INTO `meja` (`no_meja`, `keterangan`, `status_meja`) VALUES
(1, 'Indoor', 'Terisi'),
(2, 'indoor', 'Terisi'),
(3, 'Indoor', 'Terisi'),
(4, 'Indoor', 'Terisi'),
(5, 'Outdoor', 'Kosong');

-- --------------------------------------------------------

--
-- Struktur dari tabel `promo`
--

CREATE TABLE `promo` (
  `id_promo` int(255) NOT NULL,
  `menu` varchar(255) NOT NULL,
  `harga_awal` double(10,2) NOT NULL,
  `harga_promo` double(10,2) NOT NULL,
  `tanggal` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `promo`
--

INSERT INTO `promo` (`id_promo`, `menu`, `harga_awal`, `harga_promo`, `tanggal`) VALUES
(1, 'Bakso', 13000.00, 10000.00, '2023-01-12'),
(7, 'Sushi', 15000.00, 120000.00, '2023-01-11'),
(10, 'Makanan', 10000.00, 10000.00, '2023-01-19');

-- --------------------------------------------------------

--
-- Struktur dari tabel `reservasi`
--

CREATE TABLE `reservasi` (
  `id_pemesanan` int(11) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `telp` varchar(15) DEFAULT NULL,
  `jum_tamu` int(3) DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  `jam` time NOT NULL,
  `tambahan` varchar(255) DEFAULT NULL,
  `id_user` int(11) NOT NULL,
  `meja_no` int(11) NOT NULL,
  `ket_meja` varchar(255) DEFAULT NULL,
  `status` varchar(255) NOT NULL,
  `identitas` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `reservasi`
--

INSERT INTO `reservasi` (`id_pemesanan`, `nama`, `email`, `telp`, `jum_tamu`, `tanggal`, `jam`, `tambahan`, `id_user`, `meja_no`, `ket_meja`, `status`, `identitas`) VALUES
(1, 'aryaputra', 'kinsglaive34@gmail.com', '0127777', 3, '2023-01-05', '07:41:48', 'Bangku Bayi', 2, 2, 'Outdoor', 'Selesai', NULL),
(2, 'Deni', 'email@email.com', '321321', 2, '2023-01-04', '22:03:10', 'tidak ada', 2, 3, 'Outdoor', 'Selesai', NULL),
(7, 'Sagiri', 'Sagiri@gmail.com', '08154845898', 2, '2023-01-11', '21:33:00', 'Tidak ada', 2, 1, 'Outdoor', 'Pending', NULL),
(8, 'Angelina', 'Angelina@gmail.com', '081546578456', 2, '2023-01-11', '21:34:00', 'Tidak ada', 2, 4, 'Outdoor', 'Selesai', NULL),
(9, 'Ilman', 'ilman@ilman', '123456789', 3, '2023-01-18', '07:43:00', 'tidak ada', 2, 3, 'Outdoor', 'Pending', NULL),
(10, '123', '123@aqe', '123', 3, '2023-01-18', '08:03:00', 'we', 2, 2, 'indoor', 'Pending', '../static/img/a0000370_main.png'),
(11, 'orang orangan', 'aryaputramaheswara34@gmail.com', '081546578456', 3, '2023-01-03', '08:11:00', 'tidak ada', 2, 4, 'Indoor', 'Pending', '../static/img/orangutan.jpg');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id_user` int(255) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id_user`, `username`, `password`) VALUES
(1, 'admin', '321'),
(2, 'Sagiri', '1234'),
(4, 'Welty', '1111');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `daftar_menu`
--
ALTER TABLE `daftar_menu`
  ADD PRIMARY KEY (`id_menu`),
  ADD KEY `menu` (`menu`),
  ADD KEY `harga` (`harga`);

--
-- Indeks untuk tabel `meja`
--
ALTER TABLE `meja`
  ADD PRIMARY KEY (`no_meja`),
  ADD KEY `keterangan` (`keterangan`);

--
-- Indeks untuk tabel `promo`
--
ALTER TABLE `promo`
  ADD PRIMARY KEY (`id_promo`),
  ADD KEY `harga_awal` (`harga_awal`),
  ADD KEY `menu` (`menu`);

--
-- Indeks untuk tabel `reservasi`
--
ALTER TABLE `reservasi`
  ADD PRIMARY KEY (`id_pemesanan`),
  ADD KEY `id_user` (`id_user`),
  ADD KEY `meja_no` (`meja_no`),
  ADD KEY `ket_meja` (`ket_meja`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `daftar_menu`
--
ALTER TABLE `daftar_menu`
  MODIFY `id_menu` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `meja`
--
ALTER TABLE `meja`
  MODIFY `no_meja` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `promo`
--
ALTER TABLE `promo`
  MODIFY `id_promo` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT untuk tabel `reservasi`
--
ALTER TABLE `reservasi`
  MODIFY `id_pemesanan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `promo`
--
ALTER TABLE `promo`
  ADD CONSTRAINT `promo_ibfk_1` FOREIGN KEY (`harga_awal`) REFERENCES `daftar_menu` (`harga`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `promo_ibfk_2` FOREIGN KEY (`menu`) REFERENCES `daftar_menu` (`menu`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `reservasi`
--
ALTER TABLE `reservasi`
  ADD CONSTRAINT `reservasi_ibfk_1` FOREIGN KEY (`meja_no`) REFERENCES `meja` (`no_meja`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reservasi_ibfk_2` FOREIGN KEY (`ket_meja`) REFERENCES `meja` (`keterangan`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `reservasi_ibfk_3` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
