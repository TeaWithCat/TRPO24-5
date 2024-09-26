# Представление поля

- На поле 10x10 клеток, у каждой из которых есть своя уникальная координата `d_cord ∈ N`, где `0 <= d_cord <= 99`. 
  Координата представлена в виде `i * 10 + j = d_cord`, где `i, j ∈ N` и `0 <= i, j <= 9`. Говоря простым языком: `f(i_cord, j_cord) = d_cord`

- Полное поле можно записать в виде полинома: P = a<sub>0</sub>a<sup>0</sup> + a<sub>1</sub>a<sup>1</sup> + a<sub>2</sub>a<sup>2</sup> + ... + a<sub>99</sub>a<sup>99</sup>, где `p_i ∈ N` и `p_i ∈ [0, 1]`.

- Если на координате `x` находится корабль, то `p_x = 1`, иначе `p_x = 0`.

# Представление корабля

Каждый корабль имеет:

- Представление в виде полинома `p_cord`: a<sub>i</sub> = 1 ↔ клетка с координатой i занята кораблем. Для дальнейших вычислений также отдельно хранятся степени полинома, для которых a<sub>i</sub> = 1.
- Представление в виде начальной координаты `d_cord`, его положения `type`: `type ∈ N`, `type ∈ [0, 1]`, где `0` - вертикальное положение, `1` - горизонтальное. А также размера `size` корабля, отвечающий за количество занимаемых им клеток. `size ∈ N`, `size ∈ [1, 4]`

Каждое представление корабля важно для работы программы!

# Описание функций и классов

## Функции

### `make_ship(self)`
- Создает представление корабля в виде начальной координаты `d_cord`, его направления `type` и его размера `size` (размер задается при инициализации класса).
- Базируясь на представлении выше, функция записывает корабль в виде полинома `p_cord` и индексов его ненулевых коэффициентов `degree`.

### `update_ship(self, amount: int)`
- Обновляет положение корабля. Сдвигает коэффициенты в полиноме `p_cord` и обновляет актуальные индексы ненулевых коэффициентов в `degree`.

## Классы

### `game`
Автор признается, что не является экспертом в ООП и подобных концепциях. Поэтому идея класса заключалась в том, чтобы собрать в нем только самую нужную информацию для работы игры. Таким образом, вся эта затея с морским боем на математике и битовых операциях имеет смысл: задействуется минимальное количество памяти, так как все остальные классы создаются только в других функциях и занимают место на стеке очень малое количество времени, так как побитовые операции выполняются быстро!

Для работы самой игры достаточно лишь знать:
1. Множество всех расставленных кораблей списком. Таким образом, мы можем идентифицировать отдельные корабли (сами корабли представлены в виде одного полинома, уже без хранения степеней).
2. Множество всех кораблей в виде одного большого полинома.
3. Множество всех координат произведенных выстрелов.

В классе есть только функции, которые влияют на ход игры. Все функции построения поля и кораблей реализованы в других частях кода.

### `math_battlefield`
Класс с функциями, ответственными за генерацию поля. Алгоритм генерации следующий:

Повторить 10 раз:
  - Создать корабль с ровно `1` использованием функции рандома `O(1)`.
  - Если корабль можно поставить на сгенерированную локацию, перейти к следующему шагу. Иначе, сдвинуть его по полю. Максимум может произойти 98 сдвигов O(98) = `O(1)`.
  - Готовый корабль сдвигается по всем возможным направлениям на `1`, создавая недоступные для расставления будущих кораблей клетки.
  - Только готовый корабль записывается в поле с одними лишь кораблями.




