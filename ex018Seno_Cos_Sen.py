from math import radians, sin, cos, tan
an = float(input('Digite o ângulo qur você deseja '))
seno = sin(radians(an))
print('O ângulo de {:.1f} tem o Seno de {:.2f}'.format(an, seno))
cos = cos(radians(an))
print('O ângulo de {:.1f} tem o Cosceno de {:.2f}'.format(an, cos))
tan = tan(radians(an))
print('O ângulo de {:.1f} tem a Tangente de {:.2f}'.format(an, tan))
