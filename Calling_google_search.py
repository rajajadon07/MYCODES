from googlesearch import search
inp=st.text_input()
query = 'inp'

for i in search(query,lang='en',start=0,num=20,end=20,pause=2):
     print(i)
