

# Yantra Patterns
A Python package for generating  yantras with Sinhala and English text.

## **Installation**
Install using `pip` after building the package:
```sh
pip install yantra_patterns
```

## **Usage**  

### **Sinhala Yantra**
```python
from yantra_patterns import sinhala

sinhala.protactive_yantra("sinhala_yantra.png")
```

![sinhala](./sinhala_yantra.png)

### **English Yantra**
```python
from yantra_patterns import english

english.protactive_yantra("english_yantra.png")
```
![english](./english_yantra.png)

## **Features**
- Generates **protective yantra patterns**  
- Supports **Sinhala and English text**  
- Uses **Pillow (PIL) for image generation**  
- Includes **custom fonts for Sinhala text**  

## **Requirements**
- Python 3.6+
- `Pillow`
- `numpy`

