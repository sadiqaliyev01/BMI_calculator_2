import streamlit as st

height = float(st.number_input("Boyunuzu daxil edin (metr ilə): "))
mass = int(st.number_input("Kütlənizi daxil edin (kq ilə): "))
age = int(st.number_input("Yaşınızı daxil edin: "))
sex = st.radio("Cinsinizi daxil edin:", ["Kişi", "Qadın"])
result=None

def vki():
  try:
    if height == 0:
      return None
    result = mass / (height * height)
  except ZeroDivisionError:
    result = None
  return result


def funk():
  if vki() is None:
    st.text("Height cannot be zero.")
  else:
    st.text('Sizin VKI-niz: {}'.format(vki()))

  if vki() < 18.5:
    st.text('''
  Zəif
  Sağlam bir kilo almağa yönəldilməlidir.
  Balanslaşdırılmış qidalanma proqramını qəbul etmək vacibdir.
  Bir məşq proqramı yaratmaqla əzələ kütləsini artırmaq olar.''')

  elif 18.5<=vki()<25:
    st.text('''
  Normal ağırlıq
  Sağlam çəkidə qalmaq üçün balanslı bir pəhriz davam etdirilməlidir.
  Aktiv həyat tərzini saxlamaq vacibdir.
  Daimi məşq ümumi sağlamlığı dəstəkləyə bilər.''')

  elif 25<=vki()<30:
   st.text('''
  Artıq çəkili
  Sağlam kilo itkisi hədəflənməlidir.
  Balanslaşdırılmış pəhriz və idman proqramı həyata keçirilməlidir.
  Dəstək bir həkim və ya diyetoloqdan alına bilər.''')

  elif 30<=vki()<35:
   st.text('''
  Piylənmə (Piylənmə - I tip)
  Nəzarətli çəki itkisi hədəflənməlidir.
  Sağlam bir pəhriz və uzunmüddətli idman proqramını qəbul etmək vacibdir.
  Peşəkar səhiyyə işçisi ilə əməkdaşlıq edilə bilər.''')

  elif 35<=vki()<40:
   st.text('''
  Piylənmə (Piylənmə - II Tip)
  Proqressiv piylənmə halında həkim nəzarəti altında xüsusi sağlamlıq proqramı yaradıla bilər.
  Diyetisyen və ya sağlamlıq mütəxəssisi ilə əməkdaşlıq vacibdir.''')

  elif vki()>=40:
   st.text('''
  Piylənmə (Morbid Piylənmə - Tip III)
  Şiddətli piylənmə hallarında tibb işçiləri tərəfindən idarə olunan xüsusi müalicə planı tələb oluna bilər.
  Cərrahi müdaxilə kimi variantlar nəzərdən keçirilə bilər.''')


if st.button("Heabla"):
  if sex == 'Qadın':
    if 18<=age<=29:
      funk()
      st.text('''
      Sizin yaşınıza görə ideal ağırlıq 73 kq-dır.''')


  elif 30<=age<=39:
    funk()
    st.text('''
    Sizin yaşınıza görə ideal ağırlıq 77 kq-dır.''')

  elif 40<=age<=49:
    funk()
    st.text('''
    Sizin yaşınıza görə ideal ağırlıq 76 kq-dır.''')

  elif 50<=age<=59:
    funk()
    st.text('''
    Sizin yaşınıza görə ideal ağırlıq 77 kq-dır.''')

  elif 60<=age<=69:
    funk()
    st.text('''
    Sizin yaşınıza görə ideal ağırlıq 75 kq-dır.''')

  elif 70<=age<=79:
    funk()
    st.text('''
    Sizin yaşınıza görə ideal ağırlıq 77 kq-dır.''')



  if sex == 'Kişi':
    if 18<=age<=29:
      funk()
      st.text('''
      Sizin yaşınıza görə ideal ağırlıq 83 kq-dır.''')

    elif 30<=age<=39:
      funk()
      st.text('''
      Sizin yaşınıza görə ideal ağırlıq 90 kq-dır.''')

    elif 40<=age<=49:
      funk()
      st.text('''
      Sizin yaşınıza görə ideal ağırlıq 91 kq-dır.''')

    elif 50<=age<=59:
      funk()
      st.text('''
      Sizin yaşınıza görə ideal ağırlıq 91 kq-dır.''')

    elif 60<=age<=69:
      funk()
      st.text('''
      Sizin yaşınıza görə ideal ağırlıq 90 kq-dır.''')

    elif 70<=age<=79:
      funk()
      st.text('''
      Sizin yaşınıza görə ideal ağırlıq 86 kq-dır.''')

#datalari input ele. vki hesabla. her vki araligina gore neticeni ve mesleheti, yasa ve cinsiyyete gore ideal cekini print ele.
#yas araliqlarina gore vki verilir. bu vki lere gore dusturdan mass tap. minimum maksimum
