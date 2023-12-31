# <span style="color:#C0BFEC">Языки прикладного программирования</span>
Лабораторная работа №4 “Интерполяция, аппроксимация, линейная регрессия”

## <span style="color:#C0BFEC">Интерполяция:
Интерполяция - это способ нахождения промежуточных значений величины по имеющемуся дискретному набору известных значений. Интерполяция использует значения некоторой функции, заданные в ряде точек, чтобы предсказать значения функции между ними.
Графически задача интерполирования заключается в том, чтобы построить такую интерполирующую функцию, которая бы проходила через все узлы интерполирования. Линейная интерполяция – простейший и часто используемый вид интерполяции. Она состоит в том, что заданные точки соединяются прямолинейными отрезками, а функцию y(x) можно приближенно представить в виде ломаной.

## <span style="color:#C0BFEC">Аппроксимация:
Аппроксимация – замена одних математических объектов другими, в том или ином смысле близкими к исходным. При интерполировании, интерполирующая функция строго проходит через узловые точки таблицы вследствие того, что количество коэффициентов в интерполирующей функции равно количеству табличных значений.
Аппроксимация – метод приближения, при котором для нахождения дополнительных значений, отличных от табличных данных, приближенная функция проходит не через узлы интерполяции, а между ними (рис. 1).

## <span style="color:#C0BFEC">Линейная регрессия:
Линейная регрессия — модель зависимости переменной x от одной или нескольких других переменных (факторов, регрессоров, независимых переменных) с линейной функцией зависимости. Цель линейной регрессии — поиск линии, которая наилучшим образом соответствует этим точкам .

## <span style="color:#C0BFEC">Полезные ссылки:
Также по данным понятиям, методам и примерам их использования можно более подробно почитать в следующих источниках:

### <span style="color:#C0BFEC">Интерполяция:
* https://habr.com/ru/post/264191/
* https://help.fsight.ru/ru/mergedProjects/lib/03_transformations/uimodelling_interpolation.htm
* https://portal.tpu.ru/SHARED/m/MBB/uchebnaya_rabota/Model/Tab/Interp_app.pdf
* http://aco.ifmo.ru/el_books/numerical_methods/lectures/glava3.html

### <span style="color:#C0BFEC">Регрессия:
* https://pythobyte.com/linear-regression-in-python-with-scikit-learn-bc1b4512/
* https://habr.com/ru/post/514818/
* http://statistica.ru/theory/osnovy-lineynoy-regressii/
* https://blog.skillfactory.ru/glossary/linejnaya-regressiya/
* https://neurohive.io/ru/osnovy-data-science/linejnaja-regressija/

## <span style="color:#C0BFEC">Задание на лабораторную работу:
1) Необходимо реализовать программу на языке Python 3, позволяющую на основании некоторой выборки данных, давать предсказания по вводимым с клавиатуры значениям входного параметра. 
2) Решать данную задачу необходимо методом линейной регрессии. 
3) Реализацию метода можно взять из библиотеки scikit. 

В качестве входных данных, можно использовать один из следующих датасетов (или любой другой подходящий, но более интересный):
* https://www.kaggle.com/dwdkills/russian-demography
* https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston
* https://www.kaggle.com/tunguz/country-regional-and-world-gdp

4) Результат - визуализировать.

5) В качестве альтернативы, вместо линейной регрессии можно решить задачу интерполяции несколькими методами (линейная, квадратичная, кубическая, сплайны), также визуализировать результаты. В качестве входных данных задаётся не выборка, а математическая функция в коде (можно сделать и ввод с клавиатуры, например с использованием функции eval) с шагом вычисления точек для исходных данных.
6) При вводе значений параметра с клавиатуры выдавать интерполированное значение функции.
7) Добавить проверку на то, что искомая точка лежит внутри известных интервалов.
8) Для оценки интерполяции, также выдавать результат сравнения результата интерполирования с значением заданной функции в данной точке.
9) Методы интерполяции также могут быть взяты из библиотеки.

* В качестве дополнительного задания, можно написать собственную реализацию линейной, кусочно-квадратичной или квадратичной интерполяции (или другой, более сложный алгоритм) на дополнительные баллы.

### <span style="color:#C0BFEC">Общие требования:
```
На каждом графике должна быть “легенда” 
Следовать принципам KISS, DRY, YAGNI и т.п.
Код должен соответствовать code-style соответствующего языка: для Python
```
