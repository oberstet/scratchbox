"""
Eine Iterator-Klasse zur Erzeugung von verallgemeinerten Lucas-Folgen U_n(P, Q) und V_n(P, Q).
"""

from typing import Iterator


class LucasSequence:
    """
    Ein Iterator zur Erzeugung von verallgemeinerten Lucas-Folgen.

    Diese Klasse implementiert die Folgen U_n(P, Q) und V_n(P, Q),
    die durch die folgende Rekurrenzrelation definiert sind:
    x_n = P * x_{n-1} - Q * x_{n-2}

    Die Startwerte sind:
    - Für die erste Art (U_n): U_0 = 0, U_1 = 1
    - Für die zweite Art (V_n): V_0 = 2, V_1 = P

    Der Iterator gibt bei jedem Schritt ein Tupel (U_n, V_n) zurück.
    """

    def __init__(self, P: int, Q: int) -> None:
        """
        Initialisiert den Lucas-Folgen-Generator.

        Args:
            P (int): Der Parameter P der Rekurrenzrelation.
            Q (int): Der Parameter Q der Rekurrenzrelation.
        """
        self.P = P
        self.Q = Q

        # Initialzustand für n=0 und n=1 für die U-Folge
        self._u_current: int = 0  # U_0
        self._u_next: int = 1  # U_1

        # Initialzustand für n=0 und n=1 für die V-Folge
        self._v_current: int = 2  # V_0
        self._v_next: int = P  # V_1

    def __iter__(self) -> Iterator[tuple[int, int]]:
        """Macht die Klasse zu einem Iterator."""
        return self

    def __next__(self) -> tuple[int, int]:
        """
        Berechnet das nächste Paar (U_n, V_n) in der Folge.

        Returns:
            Ein Tupel mit dem aktuellen U_n und V_n Wert.
        """
        # Aktuelle Werte zur Rückgabe speichern
        return_val = (self._u_current, self._v_current)

        # Die nächsten Werte in der Folge berechnen
        # x_n = P * x_{n-1} - Q * x_{n-2}
        new_u = self.P * self._u_next - self.Q * self._u_current
        new_v = self.P * self._v_next - self.Q * self._v_current

        # Den Zustand für die nächste Iteration aktualisieren
        self._u_current = self._u_next
        self._v_current = self._v_next
        self._u_next = new_u
        self._v_next = new_v

        return return_val
