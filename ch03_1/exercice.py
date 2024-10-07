#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def square_root(a: float) -> float:
    sqr_root = math.sqrt(a)
    return sqr_root


def square(a: float) -> float:
    power = a**2
    return power


def average(a: float, b: float, c: float) -> float:
    moyen = (a+b+c)/3
    return moyen


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    rads = math.radians(angle_degs + (angle_mins + (angle_secs/60))/60)

    return rads


def to_degrees(angle_rads: float) -> tuple:

    degs = math.degrees(angle_rads)

    minutes = (abs(degs) - int(abs(degs)))*60

    seconds = (minutes - int(abs(minutes)))*60

    return round(degs, 0), round(minutes, 0), round(seconds, 0)


def to_celsius(temperature: float) -> float:
    celsius = (temperature - 32)/1.8
    return celsius


def to_farenheit(temperature: float) -> float:
    fahren = temperature*1.8 + 32
    return fahren


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
