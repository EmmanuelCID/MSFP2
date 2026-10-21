[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=l23212186-ops/MSFP2)

# Práctica 2: Modelado y control del sistema cardiovascular mediante el modelo Windkessel.

## Información del estudiante
Emmanuel Cid Pacheco [23212187]; L23212187@tectijuana.edu.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente
Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Determinar el modelo de ecuaciones diferenciales del modelo Windkessel de cuatro elementos.
2. Calcular la función de transferencia de los casos hipotenso, normotenso e hipertenso.
3. Analizar la estabilidad del sistema.
4. Determinar el error en estado estacionario.
5. Simular la respuesta en lazo abierto de los tres casos en Simulink/Simscape ante una señal de excitación aleatoria.
6. Sintonizar las ganancias de un controlador PID en Simulink/MATLAB para reducir el error entre la respuesta normotensa y las respuestas hipotensa e hipertensa.
7. Simular la respuesta del sistema en lazo cerrado con el controlador PID en Simulink/MATLAB.
8. Obtener la respuesta en lazo abierto y en lazo cerrado con el controlador PID en Python con la función de transferencia.

## Descripción detallada del sistema

En esta práctica se estudia el modelado y control del sistema cardiovascular mediante el modelo Windkessel, el cual establece una analogía fundamental entre las propiedades elásticas de las arterias (compliancia), la resistencia periférica al flujo sanguíneo y los elementos pasivos de un circuito $RLC$. El sistema modela la dinámica de la presión y el flujo en el aparato circulatorio, permitiendo evaluar la respuesta transitoria y estacionaria ante perturbaciones, así como el desempeño de estrategias de control clásico para la regulación hemodinámica.

Palabras clave: Sistema cardiovascular; Modelo Windkessel; Circuito RLC; Controlador PID; Simulación numérica.

## Lista de archivos incluidos en el repositorio
1. Cuaderno computacional de MATLAB \[.mlx].
2. Modelo de Simulink \[.slx].
3. Archivos de VS Python \[.py].
4. Imagen con los parámetros de ambos controladoradores.
5. Imágenes de las simulaciones \[.pdf].
6. Imagen de diagrama biologico.
7. Análisis matemático: Función de transferencia, modelo de ecuaciones integro-diferenciales, estabilidad y error en estado estacionario.

## Referencias
\[1] M. C. Khoo, Physiological Control Systems: Analysis, Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018.

\[2] F. C. Hoppensteadt and C. S. Peskin, Modeling and Simulation in Medicine and the Life Sciences, 2nd ed. New York, NY, USA: Springer, 2002.

\[3] J. E. Hall, Guyton and Hall Textbook of Medical Physiology, 14th ed. Philadelphia, PA, USA: Elsevier, 2021.

\[4] K. Ogata, Ingeniería de Control Moderna, 5a ed. Madrid, España: Pearson Educación, 2010.

\[5] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.

\[6] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026. Permalink: https://biomath.xyz/course/

\[7] Tecnológico Nacional de México, Programa de estudio de la asignatura Modelado de Sistemas Fisiológicos, Clave de la asignatura: IBF-1020, 2010.
