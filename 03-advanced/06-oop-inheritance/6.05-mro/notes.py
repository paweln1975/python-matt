#!/usr/bin/env python3
# https://python3.info/advanced/oop-inheritance/mro.html


# %% Inheritance MRO
# - MRO - Method Resolution Order
# - Inheritance Diamond
# %%



# %% Show MRO
# - cls.mro()
# - cls.__mro__
# %%



# %% Small Diamond
# %%



# %% Large Diamond
# %%



# %% Algorithm
# - Source: [#Halterman2018]_
# - Source: [#StackOverflowMRO]_
# %%



# %% Inconsistent MRO
# %%



# %% Further Reading
# - van Rossum, G. Method Resolution Order. Year: 2010. Retrieved: 2022-07-13. URL: http://python-history.blogspot.com/2010/06/method-resolution-order.html
# - Hettinger R. Super considered super!. PyCon 2015. Year: 2020. Retrieved: 2022-07-13. URL: https://www.youtube.com/watch?v=EiOglTERPEo
# %%

class DoughFactory:
    def get_dough(self):
        return 'dough prepared from insecticide wheat'

class OrganicDoughFactory(DoughFactory):
    def get_dough(self):
        return 'dough prepared from pure wheat'

class Pizza(DoughFactory):

    def order_pizza(self, *toppings):
        dough = super().get_dough()
        print(dough)
        for topping in toppings:
            print(f'Adding {topping=} to dough')

class OrganicPizza(Pizza, OrganicDoughFactory):
    pass

if __name__ == '__main__':
    OrganicPizza().order_pizza('Pepperoni', 'Cheese')
    help(OrganicPizza)