import streamlit as st
import streamlit.components.v1 as components

data = [
    {
        'category' : 'Bmw',
        'url':'https://www.carscoops.com/wp-content/uploads/2020/05/2021-BMW-5-Series-Sedan-Touring-02.jpg',
        'name':'Bmw 520i',
        'price':'5000원'
    },
    {
        'category' : 'Bmw',
        'url':'https://th.bing.com/th/id/OIP.LL37pNU3hxa26cbenrfxIwHaEe?pid=ImgDet&w=1600&h=966&rs=1',
        'name':'Bmw 720i',
        'price':'7000원'
    },
    {
        'category' : 'Bmw',
        'url':'https://th.bing.com/th/id/OIP.3yj6Ucwq9VFaDDy9LET-VgHaEc?pid=ImgDet&rs=1',
        'name':'Bmw 320d',
        'price':'3000원'
    },
    {
        'category' : 'Mercedes-Benz',
        'url':'https://blog.kakaocdn.net/dn/o13a7/btq4XW8wW4j/C9wyhkD7rccQru2VMAGus1/img.png',
        'name':'E250',
        'price':'98,900,000원'
    },
    {
        'category' : 'Mercedes-Benz',
        'url':'https://kr.imboldn.com/wp-content/uploads/2022/06/2023-Mercedes-Benz-GLC-03.jpg',
        'name':'GLC300d',
        'price':'67,900,000원'
    },
    {
        'category' : 'Mercedes-Benz',
        'url':'https://media.autoexpress.co.uk/image/private/s--X-WVjvBW--/f_auto,t_content-image-full-desktop@1/v1651164579/autoexpress/2022/04/Mercedes-AMG%20GT%204-Door%2063%20S%20E-Performance.jpg',
        'name':'Mercedes-AMG GT4 Door Coupe',
        'price':'135,900,000원'
    },
    {
        'category' : 'Hyundai',
        'url':'https://www.motorgraph.com/news/photo/202208/30521_96337_466.jpg',
        'name':'Ionic 6',
        'price':'56,000,000원'
    },
    {
        'category': 'Hyundai',
        'url':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAmOMjPshTtht-GPrB3pqUxswQ8UOTMJGa2w&usqp=CAU',
        'name':'Avante-N',
        'price':'36,000,000원'
    },
    {
        'category': 'Hyundai',
        'url':'https://img1.daumcdn.net/thumb/S720x440ht.u/?fname=%2Fmedia%2Fvitraya%2Fauto%2Fimage%2F8c343c%2F574691FAF8211C9B0062C36B47DAB069D716EF12D7C7683B36_3JA1&scode=media',
        'name':'Palisade',
        'price':'59,900,000원'
    },
]



def carCard(menu):
    result =''
    for value in data:
        if value['category'] == menu:
            result = result + f"""
                <div class="col">
                    <div class="card" style="width: 18rem;">
                        <img src="{value['url']}" width="200px" height="200px" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">{value['name']}</h5>
                            <p class="card-text">{value['price']}</p>
                            </div>
                        </div>
                    </div>
            """

    return result


st.set_page_config(
    page_title='구암고',
    page_icon='😎',
    layout='wide',
    initial_sidebar_state="collapsed"
)

btn = st.button('풍선')
if btn:
    st.balloons()

menu = st.sidebar.selectbox('자동차', ('Bmw', 'Mercedes-Benz','Hyundai'))


components.html(
        f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>

    <div class="container">
      <div class="row">
         {carCard(menu = menu)}
      </div>
    </div>

    """, height=800
)



