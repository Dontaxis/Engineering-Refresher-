#!/usr/bin/env python3
"""
Engineering Fundamentals Mini-Games Collection
Interactive games to practice key engineering concepts

Run this file and play through various engineering challenges!
"""

import random
import math

# =============================================================================
# GAME CLASS
# =============================================================================

class EngineeringGames:
    def __init__(self):
        self.player_name = ""
        self.total_score = 0
        self.games_played = 0
        self.achievements = []

    def display_menu(self):
        """Display the main game menu"""
        print("\n" + "="*60)
        print("  ENGINEERING FUNDAMENTALS MINI-GAMES")
        print("="*60)
        print(f"  Player: {self.player_name}")
        print(f"  Total Score: {self.total_score} | Games Played: {self.games_played}")
        print("-"*60)
        print("  1. Force Vector Challenge")
        print("  2. Free Body Diagram Quiz")
        print("  3. Unit Conversion Speed Round")
        print("  4. Stress & Strain Problems")
        print("  5. Beam Loading Quiz")
        print("  6. Material Properties Match")
        print("  7. View Achievements")
        print("  8. Exit")
        print("="*60)

    def start_game(self):
        """Main game loop"""
        print("\n" + "="*60)
        print("  Welcome to Engineering Mini-Games!")
        print("="*60)
        self.player_name = input("  Enter your name: ").strip() or "Engineer"

        while True:
            self.display_menu()
            try:
                choice = input("\n  Select a game (1-8): ").strip()

                if choice == '1':
                    self.force_vector_game()
                elif choice == '2':
                    self.free_body_diagram_game()
                elif choice == '3':
                    self.unit_conversion_game()
                elif choice == '4':
                    self.stress_strain_game()
                elif choice == '5':
                    self.beam_loading_game()
                elif choice == '6':
                    self.material_properties_game()
                elif choice == '7':
                    self.show_achievements()
                elif choice == '8':
                    self.exit_game()
                    break
                else:
                    print("  Invalid choice! Please enter 1-8.")

            except KeyboardInterrupt:
                print(f"\n\n  Goodbye, {self.player_name}!")
                break

    def add_achievement(self, achievement):
        """Add an achievement if not already earned"""
        if achievement not in self.achievements:
            self.achievements.append(achievement)
            print(f"\n  *** NEW ACHIEVEMENT: {achievement} ***")

    def show_achievements(self):
        """Display earned achievements"""
        print("\n" + "="*60)
        print("  YOUR ACHIEVEMENTS")
        print("="*60)
        if self.achievements:
            for i, ach in enumerate(self.achievements, 1):
                print(f"  {i}. {ach}")
        else:
            print("  No achievements yet. Keep playing!")
        print("="*60)
        input("  Press Enter to continue...")

    def exit_game(self):
        """Exit with summary"""
        print("\n" + "="*60)
        print(f"  Thanks for playing, {self.player_name}!")
        print(f"  Final Score: {self.total_score}")
        print(f"  Games Played: {self.games_played}")
        print(f"  Achievements: {len(self.achievements)}")
        print("="*60)

    # =========================================================================
    # GAME 1: FORCE VECTOR CHALLENGE
    # =========================================================================

    def force_vector_game(self):
        """Force Vector Addition Challenge"""
        print("\n" + "="*60)
        print("  FORCE VECTOR CHALLENGE")
        print("  Add forces in 2D to find the resultant!")
        print("="*60)

        score = 0
        rounds = 5

        for round_num in range(1, rounds + 1):
            print(f"\n  --- Round {round_num}/{rounds} ---")

            # Generate two random forces
            f1_mag = random.randint(10, 50) * 2  # Even numbers
            f1_angle = random.choice([0, 30, 45, 60, 90, 120, 135, 150, 180])
            f2_mag = random.randint(10, 50) * 2
            f2_angle = random.choice([0, 30, 45, 60, 90, 120, 135, 150, 180])

            print(f"  Force 1: {f1_mag} N at {f1_angle} degrees from +x axis")
            print(f"  Force 2: {f2_mag} N at {f2_angle} degrees from +x axis")

            # Calculate correct answer
            f1_x = f1_mag * math.cos(math.radians(f1_angle))
            f1_y = f1_mag * math.sin(math.radians(f1_angle))
            f2_x = f2_mag * math.cos(math.radians(f2_angle))
            f2_y = f2_mag * math.sin(math.radians(f2_angle))

            result_x = f1_x + f2_x
            result_y = f1_y + f2_y
            result_mag = math.sqrt(result_x**2 + result_y**2)

            print(f"\n  What is the MAGNITUDE of the resultant force?")
            print(f"  (Hint: Fx = {result_x:.1f} N, Fy = {result_y:.1f} N)")

            try:
                user_mag = float(input("  Your answer (N): "))

                error = abs(user_mag - result_mag)

                if error <= 1:
                    points = 20
                    print(f"  Excellent! Correct: {result_mag:.1f} N")
                elif error <= 5:
                    points = 15
                    print(f"  Good! Answer: {result_mag:.1f} N (you: {user_mag:.1f})")
                elif error <= 10:
                    points = 10
                    print(f"  Close! Answer: {result_mag:.1f} N (you: {user_mag:.1f})")
                else:
                    points = 0
                    print(f"  Not quite. Answer: {result_mag:.1f} N")

                print(f"  Points: +{points}")
                score += points

            except ValueError:
                print("  Invalid input! Skipping...")

        print(f"\n  Game Over! Score: {score}/{rounds*20}")
        self.total_score += score
        self.games_played += 1

        if score >= 80:
            self.add_achievement("Vector Master")
        if score == 100:
            self.add_achievement("Perfect Vectors")

        input("  Press Enter to continue...")

    # =========================================================================
    # GAME 2: FREE BODY DIAGRAM QUIZ
    # =========================================================================

    def free_body_diagram_game(self):
        """Free Body Diagram Identification"""
        print("\n" + "="*60)
        print("  FREE BODY DIAGRAM QUIZ")
        print("  Identify ALL forces acting on the object!")
        print("="*60)

        problems = [
            {
                'scenario': 'A block sitting stationary on a horizontal table',
                'correct': {'W', 'N'},
                'explain': 'Weight (W) down, Normal (N) up. They balance.'
            },
            {
                'scenario': 'A mass hanging motionless from a rope',
                'correct': {'W', 'T'},
                'explain': 'Weight (W) down, Tension (T) up through rope.'
            },
            {
                'scenario': 'A block stationary on a rough inclined plane',
                'correct': {'W', 'N', 'f'},
                'explain': 'Weight (W) down, Normal (N) perpendicular to slope, Friction (f) up the slope.'
            },
            {
                'scenario': 'A block pushed at CONSTANT velocity across a rough floor',
                'correct': {'W', 'N', 'f', 'F'},
                'explain': 'Weight, Normal, Applied force (F), Friction (f). Net force = 0!'
            },
            {
                'scenario': 'A mass in an Atwood machine (accelerating)',
                'correct': {'W', 'T'},
                'explain': 'Only Weight (W) and Tension (T). The mass accelerates because W != T.'
            },
            {
                'scenario': 'A car on a FRICTIONLESS banked curve at design speed',
                'correct': {'W', 'N'},
                'explain': 'Weight (W) down, Normal (N) perpendicular to bank. N provides centripetal force!'
            },
            {
                'scenario': 'A book resting on a table with your hand pushing down on it',
                'correct': {'W', 'N', 'F'},
                'explain': 'Weight, Normal (larger than W!), and Applied force from hand.'
            },
            {
                'scenario': 'A ball in free fall (ignore air resistance)',
                'correct': {'W'},
                'explain': 'Only Weight! No contact = no normal, no friction, no tension.'
            }
        ]

        # Select 5 random problems
        selected = random.sample(problems, min(5, len(problems)))
        score = 0

        print("\n  Forces to choose from:")
        print("  W = Weight    N = Normal    f = friction")
        print("  T = Tension   F = Applied force")
        print("\n  Enter forces separated by commas (e.g., W,N,f)")

        for i, prob in enumerate(selected, 1):
            print(f"\n  --- Problem {i}/5 ---")
            print(f"  {prob['scenario']}")

            user_input = input("  Forces: ").strip().upper()
            user_forces = set(f.strip() for f in user_input.split(',') if f.strip())

            correct = prob['correct']

            if user_forces == correct:
                points = 20
                print(f"  CORRECT! +{points} points")
            elif user_forces.issubset(correct) and len(user_forces) > 0:
                points = 10
                print(f"  Partially correct. Missing: {correct - user_forces}")
            elif correct.issubset(user_forces):
                points = 5
                print(f"  You included extra forces: {user_forces - correct}")
            else:
                points = 0
                print(f"  Incorrect. Correct answer: {correct}")

            print(f"  Explanation: {prob['explain']}")
            score += points

        print(f"\n  Game Over! Score: {score}/100")
        self.total_score += score
        self.games_played += 1

        if score >= 80:
            self.add_achievement("FBD Expert")
        if score == 100:
            self.add_achievement("Force Master")

        input("  Press Enter to continue...")

    # =========================================================================
    # GAME 3: UNIT CONVERSION SPEED ROUND
    # =========================================================================

    def unit_conversion_game(self):
        """Unit Conversion Speed Challenge"""
        print("\n" + "="*60)
        print("  UNIT CONVERSION SPEED ROUND")
        print("  Convert quickly and accurately!")
        print("="*60)

        conversions = [
            {'q': '1 inch = ? mm', 'a': 25.4, 'tol': 0.1},
            {'q': '1 foot = ? meters', 'a': 0.3048, 'tol': 0.01},
            {'q': '1 lb = ? N', 'a': 4.448, 'tol': 0.01},
            {'q': '1 psi = ? kPa', 'a': 6.895, 'tol': 0.01},
            {'q': '1 hp = ? watts', 'a': 746, 'tol': 5},
            {'q': '1 MPa = ? psi', 'a': 145.04, 'tol': 1},
            {'q': '100 degC = ? degF', 'a': 212, 'tol': 1},
            {'q': '1 kg = ? lbm', 'a': 2.205, 'tol': 0.01},
            {'q': '1 BTU = ? Joules', 'a': 1055, 'tol': 10},
            {'q': '1 rpm = ? rad/s', 'a': 0.1047, 'tol': 0.01},
        ]

        selected = random.sample(conversions, 5)
        score = 0

        for i, conv in enumerate(selected, 1):
            print(f"\n  Question {i}/5: {conv['q']}")

            try:
                user_ans = float(input("  Your answer: "))

                if abs(user_ans - conv['a']) <= conv['tol']:
                    points = 20
                    print(f"  Correct! {conv['a']}")
                elif abs(user_ans - conv['a']) <= conv['tol'] * 3:
                    points = 10
                    print(f"  Close! Exact: {conv['a']}")
                else:
                    points = 0
                    print(f"  Wrong. Answer: {conv['a']}")

                score += points

            except ValueError:
                print(f"  Invalid. Answer: {conv['a']}")

        print(f"\n  Game Over! Score: {score}/100")
        self.total_score += score
        self.games_played += 1

        if score >= 80:
            self.add_achievement("Unit Guru")

        input("  Press Enter to continue...")

    # =========================================================================
    # GAME 4: STRESS & STRAIN PROBLEMS
    # =========================================================================

    def stress_strain_game(self):
        """Stress and Strain Calculations"""
        print("\n" + "="*60)
        print("  STRESS & STRAIN PROBLEMS")
        print("  Calculate mechanical properties!")
        print("="*60)

        score = 0

        # Problem 1: Axial Stress
        print("\n  --- Problem 1: Axial Stress ---")
        force = random.randint(5, 50) * 1000  # N
        diameter = random.randint(10, 30)  # mm
        area = math.pi * (diameter/2)**2  # mm^2
        stress = force / area  # N/mm^2 = MPa

        print(f"  A rod with diameter {diameter} mm carries a tensile load of {force/1000:.0f} kN")
        print(f"  Calculate the axial stress in MPa")
        print(f"  (Hint: Area = pi*d^2/4 = {area:.1f} mm^2)")

        try:
            user_ans = float(input("  Stress (MPa): "))
            if abs(user_ans - stress) < 1:
                score += 25
                print(f"  Correct! {stress:.1f} MPa")
            else:
                print(f"  Answer: {stress:.1f} MPa")
        except ValueError:
            print(f"  Answer: {stress:.1f} MPa")

        # Problem 2: Strain
        print("\n  --- Problem 2: Strain ---")
        original_length = random.randint(100, 500)  # mm
        extension = random.uniform(0.1, 2.0)  # mm
        strain = extension / original_length

        print(f"  A bar of length {original_length} mm extends by {extension:.2f} mm under load")
        print(f"  Calculate the strain (as a decimal)")

        try:
            user_ans = float(input("  Strain: "))
            if abs(user_ans - strain) < 0.0001:
                score += 25
                print(f"  Correct! {strain:.6f}")
            else:
                print(f"  Answer: {strain:.6f}")
        except ValueError:
            print(f"  Answer: {strain:.6f}")

        # Problem 3: Young's Modulus
        print("\n  --- Problem 3: Young's Modulus ---")
        E_values = [70, 200, 110, 45]  # GPa for Al, Steel, Cu, Mg
        E = random.choice(E_values)
        stress_val = random.randint(50, 200)  # MPa
        strain_val = stress_val / (E * 1000)  # Convert GPa to MPa

        print(f"  A material has stress = {stress_val} MPa and strain = {strain_val:.6f}")
        print(f"  Calculate Young's Modulus in GPa")

        try:
            user_ans = float(input("  E (GPa): "))
            if abs(user_ans - E) < 2:
                score += 25
                print(f"  Correct! {E} GPa")
            else:
                print(f"  Answer: {E} GPa")
        except ValueError:
            print(f"  Answer: {E} GPa")

        # Problem 4: Factor of Safety
        print("\n  --- Problem 4: Factor of Safety ---")
        yield_strength = random.randint(200, 500)  # MPa
        working_stress = random.randint(50, 150)  # MPa
        fos = yield_strength / working_stress

        print(f"  Material yield strength: {yield_strength} MPa")
        print(f"  Working stress: {working_stress} MPa")
        print(f"  Calculate the Factor of Safety")

        try:
            user_ans = float(input("  FoS: "))
            if abs(user_ans - fos) < 0.2:
                score += 25
                print(f"  Correct! {fos:.2f}")
            else:
                print(f"  Answer: {fos:.2f}")
        except ValueError:
            print(f"  Answer: {fos:.2f}")

        print(f"\n  Game Over! Score: {score}/100")
        self.total_score += score
        self.games_played += 1

        if score >= 75:
            self.add_achievement("Stress Analyst")

        input("  Press Enter to continue...")

    # =========================================================================
    # GAME 5: BEAM LOADING QUIZ
    # =========================================================================

    def beam_loading_game(self):
        """Beam Loading and Reactions"""
        print("\n" + "="*60)
        print("  BEAM LOADING QUIZ")
        print("  Find reactions and understand beam behavior!")
        print("="*60)

        score = 0

        # Problem 1: Simply supported beam with center load
        print("\n  --- Problem 1 ---")
        L = random.randint(2, 6)  # meters
        P = random.randint(5, 20)  # kN
        R = P / 2  # Each reaction

        print(f"  Simply supported beam, length {L} m")
        print(f"  Point load {P} kN at center")
        print(f"  Find EACH support reaction (they're equal)")

        try:
            user_ans = float(input("  Reaction (kN): "))
            if abs(user_ans - R) < 0.5:
                score += 20
                print(f"  Correct! {R} kN each")
            else:
                print(f"  Answer: {R} kN each")
        except ValueError:
            print(f"  Answer: {R} kN each")

        # Problem 2: Cantilever with end load
        print("\n  --- Problem 2 ---")
        L = random.randint(1, 4)
        P = random.randint(2, 10)
        M = P * L  # Moment at fixed end

        print(f"  Cantilever beam, length {L} m")
        print(f"  Point load {P} kN at free end")
        print(f"  Find the moment at the fixed support (kN-m)")

        try:
            user_ans = float(input("  Moment (kN-m): "))
            if abs(user_ans - M) < 0.5:
                score += 20
                print(f"  Correct! {M} kN-m")
            else:
                print(f"  Answer: {M} kN-m")
        except ValueError:
            print(f"  Answer: {M} kN-m")

        # Problem 3: Beam with UDL
        print("\n  --- Problem 3 ---")
        L = random.randint(3, 8)
        w = random.randint(2, 8)  # kN/m
        total_load = w * L
        R = total_load / 2

        print(f"  Simply supported beam, length {L} m")
        print(f"  Uniformly distributed load: {w} kN/m over entire length")
        print(f"  Find EACH support reaction")

        try:
            user_ans = float(input("  Reaction (kN): "))
            if abs(user_ans - R) < 0.5:
                score += 20
                print(f"  Correct! {R} kN each (total load = {total_load} kN)")
            else:
                print(f"  Answer: {R} kN each")
        except ValueError:
            print(f"  Answer: {R} kN each")

        # Problem 4: Max bending moment
        print("\n  --- Problem 4 ---")
        L = random.randint(4, 10)
        P = random.randint(10, 30)
        M_max = P * L / 4  # For center point load

        print(f"  Simply supported beam, length {L} m")
        print(f"  Point load {P} kN at CENTER")
        print(f"  Find the MAXIMUM bending moment")
        print(f"  (Hint: For center load, M_max = PL/4)")

        try:
            user_ans = float(input("  M_max (kN-m): "))
            if abs(user_ans - M_max) < 0.5:
                score += 20
                print(f"  Correct! {M_max} kN-m")
            else:
                print(f"  Answer: {M_max} kN-m")
        except ValueError:
            print(f"  Answer: {M_max} kN-m")

        # Problem 5: Conceptual
        print("\n  --- Problem 5 (Conceptual) ---")
        print("  Where is the bending moment ZERO in a simply supported beam")
        print("  with only a center point load?")
        print("  A) At the center")
        print("  B) At the supports")
        print("  C) Nowhere - it's never zero")

        user_ans = input("  Your answer (A/B/C): ").strip().upper()
        if user_ans == 'B':
            score += 20
            print("  Correct! Moment is zero at pin/roller supports.")
        else:
            print("  Answer: B - Moment is zero at simple supports.")

        print(f"\n  Game Over! Score: {score}/100")
        self.total_score += score
        self.games_played += 1

        if score >= 80:
            self.add_achievement("Beam Bender")

        input("  Press Enter to continue...")

    # =========================================================================
    # GAME 6: MATERIAL PROPERTIES MATCH
    # =========================================================================

    def material_properties_game(self):
        """Match Materials to Properties"""
        print("\n" + "="*60)
        print("  MATERIAL PROPERTIES MATCH")
        print("  Know your engineering materials!")
        print("="*60)

        questions = [
            {
                'q': 'Which material has the highest Young\'s Modulus?',
                'opts': ['Aluminum', 'Steel', 'Copper', 'Titanium'],
                'ans': 'Steel',
                'info': 'Steel: ~200 GPa, Ti: ~110, Cu: ~110, Al: ~70'
            },
            {
                'q': 'Which is most corrosion resistant in seawater?',
                'opts': ['Carbon Steel', 'Stainless Steel', 'Cast Iron', 'Brass'],
                'ans': 'Stainless Steel',
                'info': 'Stainless steel forms protective chromium oxide layer'
            },
            {
                'q': 'Best thermal conductor among these?',
                'opts': ['Steel', 'Aluminum', 'Copper', 'Titanium'],
                'ans': 'Copper',
                'info': 'Cu: 400 W/mK, Al: 237, Steel: ~50, Ti: ~22'
            },
            {
                'q': 'Which has the lowest density?',
                'opts': ['Steel', 'Aluminum', 'Copper', 'Titanium'],
                'ans': 'Aluminum',
                'info': 'Al: 2.7 g/cm3, Ti: 4.5, Steel: 7.8, Cu: 8.9'
            },
            {
                'q': 'Best material for high-temperature turbine blades?',
                'opts': ['Aluminum', 'Nickel superalloy', 'Brass', 'Cast iron'],
                'ans': 'Nickel superalloy',
                'info': 'Ni superalloys maintain strength at very high temps'
            },
            {
                'q': 'Typical Poisson\'s ratio for metals is approximately?',
                'opts': ['0.1', '0.3', '0.5', '0.7'],
                'ans': '0.3',
                'info': 'Most metals: 0.25-0.35. Steel ~0.3, Al ~0.33'
            },
        ]

        selected = random.sample(questions, 5)
        score = 0

        for i, q in enumerate(selected, 1):
            print(f"\n  --- Question {i}/5 ---")
            print(f"  {q['q']}")
            for j, opt in enumerate(q['opts'], 1):
                print(f"    {j}. {opt}")

            try:
                user_choice = int(input("  Your choice (1-4): "))
                user_ans = q['opts'][user_choice - 1]

                if user_ans == q['ans']:
                    score += 20
                    print(f"  Correct! {q['info']}")
                else:
                    print(f"  Wrong. Answer: {q['ans']}")
                    print(f"  {q['info']}")
            except (ValueError, IndexError):
                print(f"  Invalid. Answer: {q['ans']}")

        print(f"\n  Game Over! Score: {score}/100")
        self.total_score += score
        self.games_played += 1

        if score >= 80:
            self.add_achievement("Materials Expert")

        input("  Press Enter to continue...")

# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    game = EngineeringGames()
    game.start_game()
