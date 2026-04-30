import unittest
from unittest import TestCase
from unittest.mock import patch
from dragon import Dragon


class TestName(TestCase):
    def test_name_default(self):
        with self.assertRaises(TypeError):
            dragon = Dragon()  # noqa

    def test_name_positional(self):
        dragon = Dragon("Wawelski")
        self.assertEqual(dragon.name, "Wawelski")

    def test_name_keyword(self):
        with self.assertRaises(TypeError):
            dragon = Dragon(name="Wawelski")  # noqa


class TestHealth(TestCase):
    def setUp(self):
        self.dragon = Dragon("Wawelski")

    def test_health_ge_le(self):
        self.assertGreaterEqual(self.dragon.health, Dragon.INITIAL_HEALTH_MIN)
        self.assertLessEqual(self.dragon.health, Dragon.INITIAL_HEALTH_MAX)

    def test_health_is_int(self):
        self.assertIsInstance(self.dragon.health, int)

    def test_health_random_on_each_creation(self):
        values: set[int] = {Dragon("Wawelski").health for _ in range(100)}
        self.assertGreater(len(values), 1)

    def test_health_create_many(self):
        for _ in range(10000):
            dragon = Dragon("Wawelski")
            self.assertGreaterEqual(dragon.health, Dragon.INITIAL_HEALTH_MIN)
            self.assertLessEqual(dragon.health, Dragon.INITIAL_HEALTH_MAX)

    def test_health_hasattr_INITIAL_HEALTH_MIN(self):
        self.assertTrue(hasattr(Dragon, 'INITIAL_HEALTH_MIN'))
        self.assertIsInstance(Dragon.INITIAL_HEALTH_MIN, int)
        self.assertEqual(Dragon.INITIAL_HEALTH_MIN, 50)

    def test_health_hasattr_INITIAL_HEALTH_MAX(self):
        self.assertTrue(hasattr(Dragon, 'INITIAL_HEALTH_MAX'))
        self.assertIsInstance(Dragon.INITIAL_HEALTH_MAX, int)
        self.assertEqual(Dragon.INITIAL_HEALTH_MAX, 100)

    def test_take_damage_reduces_health(self):
        before: int = self.dragon.health
        self.dragon.take_damage(20)
        self.assertEqual(self.dragon.health, before - 20)

    def test_take_damage_multiple_times(self):
        before: int = self.dragon.health
        self.dragon.take_damage(10)
        self.dragon.take_damage(10)
        self.assertEqual(self.dragon.health, before - 20)

    def test_take_damage_clamped_at_zero(self):
        self.dragon.take_damage(200)
        self.assertEqual(self.dragon.health, 0)

    def test_take_damage_health_never_negative(self):
        self.dragon.take_damage(9999)
        self.assertGreaterEqual(self.dragon.health, 0)

    def test_is_dead_returns_false_when_alive(self):
        self.assertFalse(self.dragon.is_dead())

    def test_is_dead_returns_true_when_health_zero(self):
        self.dragon.take_damage(9999)
        self.assertTrue(self.dragon.is_dead())

    def test_is_dead_exact_zero(self):
        health: int = self.dragon.health
        self.dragon.take_damage(health)
        self.assertEqual(self.dragon.health, 0)
        self.assertTrue(self.dragon.is_dead())

    def test_health_default_patch(self):
        with patch('random.randint', return_value=74):
            dragon = Dragon("Wawelski")
        self.assertEqual(dragon.health, 74)


class TestPosition(TestCase):
    def setUp(self):
        self.dragon = Dragon("Wawelski", pos_x=10, pos_y=20)

    def test_position_default(self):
        dragon = Dragon("Wawelski")
        self.assertEqual(dragon.get_position(), (0, 0))

    def test_position_set_in_constructor(self):
        self.assertEqual(self.dragon.get_position(), (10, 20))

    def test_set_position_x_only(self):
        self.dragon.set_position(pos_x=5)
        self.assertEqual(self.dragon.get_position(), (5, 0))

    def test_set_position_y_only(self):
        self.dragon.set_position(pos_y=5)
        self.assertEqual(self.dragon.get_position(), (0, 5))

    def test_move_right_and_down(self):
        self.dragon.move(down=2, right=3)
        self.assertEqual(self.dragon.get_position(), (13, 22))

    def test_move_multiple_directions(self):
        self.dragon.move(up=1, left=2, down=3, right=4)
        self.assertEqual(self.dragon.get_position(), (12, 22))

    def test_move_dead_dragon_raises(self):
        self.dragon.take_damage(9999)
        with self.assertRaises(ValueError):
            self.dragon.move(down=2, right=3)

    def test_move_updates_x_right(self):
        self.dragon.move(right=5)
        self.assertEqual(self.dragon.get_position(), (15, 20))

    def test_move_updates_x_left(self):
        self.dragon.move(left=3)
        self.assertEqual(self.dragon.get_position(), (7, 20))

    def test_move_updates_y_down(self):
        self.dragon.move(down=4)
        self.assertEqual(self.dragon.get_position(), (10, 24))

    def test_move_updates_y_up(self):
        self.dragon.move(up=2)
        self.assertEqual(self.dragon.get_position(), (10, 18))


class TestMakeDamage(TestCase):
    def setUp(self):
        self.dragon = Dragon("Wawelski")

    def test_make_damage_returns_int(self):
        self.assertIsInstance(self.dragon.make_damage(), int)

    def test_make_damage_ge_min(self):
        for _ in range(100):
            self.assertGreaterEqual(Dragon("Wawelski").make_damage(), Dragon.DAMAGE_MIN)

    def test_make_damage_le_max(self):
        for _ in range(100):
            self.assertLessEqual(Dragon("Wawelski").make_damage(), Dragon.DAMAGE_MAX)

    def test_make_damage_random(self):
        values: set[int] = {Dragon("Wawelski").make_damage() for _ in range(1000)}
        self.assertGreater(len(values), 1)

    def test_health_hasattr_DAMAGE_MIN(self):
        self.assertTrue(hasattr(Dragon, 'DAMAGE_MIN'))
        self.assertIsInstance(Dragon.DAMAGE_MIN, int)
        self.assertEqual(Dragon.DAMAGE_MIN, 5)

    def test_health_hasattr_DAMAGE_MAX(self):
        self.assertTrue(hasattr(Dragon, 'DAMAGE_MAX'))
        self.assertIsInstance(Dragon.DAMAGE_MAX, int)
        self.assertEqual(Dragon.DAMAGE_MAX, 20)


if __name__ == "__main__":
    unittest.main()
