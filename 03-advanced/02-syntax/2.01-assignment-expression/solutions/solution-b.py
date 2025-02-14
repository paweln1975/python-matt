result = [(firstname, lastname)
          for line in lines
          if (records := line.split(','))
          and (firstname := records[0])
          and (lastname := records[1])
          and (age := records[2])
          and int(age) >= 40]