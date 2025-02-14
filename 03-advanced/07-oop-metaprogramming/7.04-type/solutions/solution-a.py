def factory(row):
    *values, species = row
    clsname = species.capitalize()
    cls = type(clsname, (Iris,), {})
    return cls(*values)

result = map(factory, DATA[1:])


# %% Alternatively
result = [cls(*values)
          for *values,species in DATA[1:]
          if (clsname := species.capitalize())
          and (cls := type(clsname, (Iris,), {}))]