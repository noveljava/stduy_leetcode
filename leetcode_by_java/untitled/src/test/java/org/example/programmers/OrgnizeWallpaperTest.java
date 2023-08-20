package org.example.programmers;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

class OrgnizeWallpaperTest {
    OrgnizeWallpaper orgnizeWallpaper = new OrgnizeWallpaper();

    @Test
    void solution() {
        String[] wallpaper = {".#...", "..#..", "...#."};
        int[] expected = {0, 1, 3, 4};
        int[] actual = orgnizeWallpaper.solution(wallpaper);
        assertArrayEquals(expected, actual);
    }

    @Test
    void asdlkjflqjwr() {
        String[] wallpaper = {".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."};
        int[] expected = {0, 0, 7, 9};
        int[] actual = orgnizeWallpaper.solution(wallpaper);
        assertArrayEquals(expected, actual);
    }

}