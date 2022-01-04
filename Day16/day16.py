data = open('day16.txt').readlines()[0]

def hex_to_bin(c):
    l=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    a='0123456789ABCDEF'
    return(l[a.index(c)])

def transform_data(data):
    c=''
    for e in data:
        c+=hex_to_bin(e)
    return(c)

def find_version(d):return(int(d[:3],2))
def find_type(d):return(int(d[:3],2))


#Dans une première partie on va simplement retrouver les différents formats et sommer les versions.
#Il faut donc arriver à trouver quels sont les types plutot que de savoir qui est quoi.

#La première étape est de trier par type -> on va retrouver le type à chaque fois et voir si c'est une "literal value"
#un "operator" (qui peut en contenir d'autres.)
