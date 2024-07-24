<svg width="400" height="200" xmlns="http://www.w3.org/2000/svg">
  <path d="M 10 100 C 100 0, 200 200, 300 100" 
        stroke="blue" 
        stroke-width="4" 
        fill="none" 
        stroke-dasharray="300" 
        stroke-dashoffset="300">
    <animate attributeName="stroke-dashoffset" 
             from="300" 
             to="0" 
             dur="3s" 
             fill="freeze" />
  </path>
</svg>


Конечно! Вот несколько примеров SVG-анимации с использованием функции animateTransform, которая позволяет анимировать трансформации, такие как перемещение, вращение и масштабирование.

### Пример 1: Вращение круга

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="100" r="50" fill="orange">
    <animateTransform attributeName="transform"
                      attributeType="XML"
                      type="rotate"
                      from="0 100 100"
                      to="360 100 100"
                      dur="5s"
                      repeatCount="indefinite" />
  </circle>
</svg>


### Пример 2: Масштабирование квадрата

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect x="75" y="75" width="50" height="50" fill="green">
    <animateTransform attributeName="transform"
                      attributeType="XML"
                      type="scale"
                      from="1 1"
                      to="1.5 1.5"
                      dur="2s"
                      begin="0s; scale.end+1s"
                      fill="freeze" 
                      id="scale" />
    <animateTransform attributeName="transform"
                      attributeType="XML"
                      type="scale"
                      from="1.5 1.5"
                      to="1 1"
                      dur="2s"
                      begin="scale.end"
                      fill="freeze" />
  </rect>
</svg>


### Пример 3: Перемещение звезды

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <polygon points="100,10 120,190 10,70 190,70 80,190"
           fill="purple">
    <animateTransform attributeName="transform"
                      attributeType="XML"
                      type="translate"
                      from="-50 0"
                      to="50 0"
                      dur="3s"
                      repeatCount="indefinite" />
  </polygon>
</svg>


### Пример 4: Комбинированная анимация (вращение и масштабирование)

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="100" r="30" fill="red">
    <animateTransform attributeName="transform"
                      attributeType="XML"
                      type="rotate"
                      from="0 100 100"
                      to="360 100 100"
                      dur="4s"
                      repeatCount="indefinite" />
    <animateTransform attributeName="transform"
                      attributeType="XML"
                      type="scale"
                      from="1 1"
                      to="2 2"
                      dur="2s"
                      begin="0s; rotate.end+0.5s"
                      fill="freeze" />
    <animateTransform attributeName="transform"
                      attributeType="XML"
                      type="scale"
                      from="2 2"
                      to="1 1"
                      dur="2s"
                      begin="scale.end+0.5s"
                      fill="freeze" />
  </circle>
</svg>


### Объяснение:

- **animateTransform**: Этот элемент позволяет анимировать трансформации. Вы можете указать тип трансформации (например, rotate, scale, translate).
- from и to: Эти атрибуты определяют начальное и конечное состояние трансформации.
-imateTran Длительность анимации.
- repeatCount: Определяет, сколько раз анимация будет повторяться (например, indefinite для бесконечного повторения).
- begin: Позволяет задать время начала анимации, что позволяет создавать сложные последовательности.

Вы можете вставить любой из этих примеров в HTML-документ и открыть его в браузере, чтобы увидеть анимацию в действии!




Конечно! Функция animateMotion в SVG позволяет анимировать движение объектов по заданной траектории. Ниже приведены несколько примеров, демонстрирующих различные возможности animateMotion.

### Пример 1: Движение по прямой линии

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="20" cy="100" r="10" fill="blue">
    <animateMotion dur="3s" repeatCount="indefinite">
      <mpath href="#path1" />
    </animateMotion>
  </circle>
  <path id="path1" d="M 20,100 L 180,100" stroke="none" fill="none"/>
</svg>


### Пример 2: Движение по круговой траектории

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="100" r="10" fill="red">
    <animateMotion dur="4s" repeatCount="indefinite">
      <mpath href="#circlePath" />
    </animateMotion>
  </circle>
  <path id="circlePath" d="M 100,100 m -50, 0 a 50,50 0 1,0 100,0 a 50,50 0 1,0 -100,0" fill="none"/>
</svg>


### Пример 3: Движение по произвольной траектории

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="20" height="20" fill="green">
    <animateMotion dur="5s" repeatCount="indefinite">
      <mpath href="#customPath" />
    </animateMotion>
  </rect>
  <path id="customPath" d="M 10,10 C 80,0 80,200 10,190 S 0,50 10,10" fill="none"/>
</svg>


### Пример 4: Движение с изменением направления

<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">
  <circle cx="150" cy="150" r="10" fill="purple">
    <animateMotion dur="6s" repeatCount="indefinite">
      <mpath href="#zigzagPath" />
    </animateMotion>
  </circle>
  <path id="zigzagPath" d="M 150,150 L 250,50 L 50,50 L 150,150 Z" fill="none"/>
</svg>


### Объяснение:

- **animateMotion**: Этот элемент используется для анимации движения объекта по заданной траектории.
- mpath: Этот элемент определяет путь, по которому будет двигаться анимируемый объект. Он ссылается на элемент <path>, который описывает саму траекторию.
- dur: Длительность анимации.
-otion в SVG позво Определяет количество повторений анимации (например, indefinite для бесконечного повторения).
- path: Элемент <path> описывает форму траектории с помощью атрибута d.

Вы можете вставить любой из этих примеров в HTML-документ и открыть его в браузере, чтобы увидеть анимацию в действии!
