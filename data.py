import streamlit as st

one_data_gpt_predefinded = """
Arca Continental, one of the world's largest Coca-Cola bottlers, has announced a new long-term agreement with The Coca-Cola Company. This agreement aims to strengthen the collaboration and relationship between both companies. The scope of the agreement includes all markets served by Arca Continental in Mexico, Ecuador, Peru, and Argentina, and it consolidates avenues for joint value creation¹²³.
The partnership also opens up possible opportunities for innovation in commercial aspects and in the portfolio. Additionally, The Coca-Cola Company will hold a 20% stake in the planned Arca Continental Beverages Business, which will operate in new territories in the United States, as well as existing territories in Mexico, Argentina, Ecuador, and Peru⁴.
For more detailed information on their agreements and operations, you can visit the official Arca Continental website or read the latest press releases on this topic.
"""


two_data_gpt_predefinded = """
Coca-Cola's inventory refers to the total value of their products in all stages of completion. As of March 31, 2024, Coca-Cola's inventory was valued at $4.961 billion, which is a 4.95% increase year-over-year. The inventory for 2023 was $4.424 billion, marking a steady growth from the previous years¹².
Regarding their products, Coca-Cola offers a wide range of beverages that include not only the trademark Coca-Cola but also sports drinks, juice and dairy drinks, alcohol ready-to-drink beverages, and more. They have a diverse portfolio of brands that are popular in North America and around the world³.
The Coca-Cola System is their primary distribution method, where Coca-Cola manufactures and sells concentrates, beverage bases, and syrups to bottling operations. They also own the brands and are responsible for consumer brand marketing initiatives⁴.
For a detailed list of Coca-Cola's products and brands, you can visit their official website.
"""

three_data_gpt_predefinded = ""
if st.session_state.name=="Carlos Flores":
    three_data_gpt_predefinded += """
Prompt para un usuario de ChatGPT:
"¿Cuáles promociones hay actualmente disponibles para los productos de Coca-Cola?"
Respuesta de ChatGPT:
Las promociones actuales disponibles para los productos de Coca-Cola son:
Promoción 1:
Descripción: 10% de descuento en los botellones de Ciel.
Promoción 2:
Descripción: Recibe una lata de Coca-Cola sin azúcar por cada diez latas de Coca-Cola compradas.
Promoción 3:
Descripción: Combo de 8 botellas de Coca-Cola de 2.0L y 24 botellas de Ciel de 235ml a $300.
Entiendo, aquí están las tres promociones que mencionaste:
Promoción 1:
10% en los botellones Ciel
Promoción 2:
Una lata de Coca-Cola sin azúcar por cada diez latas de Coca-Cola
Promoción 3:
Combo de 8 Botellas Coca Cola de 2.0L y 24 Botellas Ceil de 235ml a $300
Estas promociones están diseñadas para ofrecer descuentos y beneficios adicionales al comprar productos específicos de la línea de bebidas de la familia Coca-Cola.
"""
elif st.session_state.name=="Alejandro Acosta":
    three_data_gpt_predefinded += """
Prompt para un usuario de ChatGPT:
"¿Cuáles promociones hay actualmente disponibles para los productos de Coca-Cola?"
Respuesta de ChatGPT:
Las promociones actuales disponibles para los productos de Coca-Cola son:
Promoción 1:
Descripción: Descuento del 20% en todas las latas de Sprite y Fanta.
Promoción 2:
Descripción: Recibe una botella de Fanta de litro por cada cinco botellas de litro de Coca-Cola compradas.
Promoción 3:
Descripción: Combo de 12 botellas de Sprite de 1.0L y 24 botellas de Fanta de 500ml a $470.
Promoción 1:
Descuento del 20% en todas las latas de Sprite y Fanta
Promoción 2:
Una botella Fanta de litro por cada cino bottelas de litro de Coca-Cola
Promoción 3:
Combo de 12 Botellas Sprite de 1.0L y 24 botellas Fanta de 500ml a $470
Estas promociones están diseñadas para ofrecer descuentos y beneficios adicionales al comprar productos específicos de la línea de bebidas de la familia Coca-Cola.
    """
elif st.session_state.name=="Hector Molino":
    three_data_gpt_predefinded += """
Prompt para un usuario de ChatGPT:
"¿Cuáles promociones hay actualmente disponibles para los productos de Coca-Cola?"
Respuesta de ChatGPT:
Las promociones actuales disponibles para los productos de Coca-Cola son:
Promoción 1:
Descripción: 5 pesos menos a cada botella de 2L de Coca-Cola sin azúcar.
Promoción 2:
Descripción: Recibe una lata de Coca-Cola sin azúcar por cada diez latas de Coca-Cola compradas.
Promoción 3:
Descripción: Combo de 8 botellas de Coca-Cola de 2.0L y 24 botellas de Ciel de 235ml a $300.
Promoción 1:
5 pesos menos a cada botella de 2L de Coca-Cola sin azúcar
Promoción 2:
Una lata de Coca-Cola sin azúcar por cada diez latas de Coca-Cola
Promoción 3:
Cobmo de 8 Botellas Coca Cola de 2.0L y 24 Botellas Ceil de 235ml a $300
Estas promociones están diseñadas para ofrecer descuentos y beneficios adicionales al comprar productos específicos de la línea de bebidas de la familia Coca-Cola.
    """
elif st.session_state.name=="Jessica Paz":
    three_data_gpt_predefinded += """
Prompt para un usuario de ChatGPT:
"¿Cuáles promociones hay actualmente disponibles para los productos de Coca-Cola?"
Respuesta de ChatGPT:
Las promociones actuales disponibles para los productos de Coca-Cola son:
Promoción 1:
Descripción: Descuento del 10% en todas las botellas Powerade.
Promoción 2:
Descripción: Recibe una botella de Vitamin Water de 500ml por cada six-pack de Powerade comprados.
Promoción 3:
Descripción: Combo de 6 botellas de Powerade de 1.0L y 6 botellas de Vitamin Water a $250.
Promoción 1:
Descuento del 10% en todas las botellas Powerade
Promoción 2:
Una botella Vitamin Water de 500ml por cada six-pack de Powerade
Promoción 3:
Combo de 6 botellas Poweradede 1.0L y 6 botellas Vitamina Water a $250
Estas promociones están diseñadas para ofrecer descuentos y beneficios adicionales al comprar productos específicos de la línea de bebidas de la familia Coca-Cola.
    """
elif st.session_state.name=="Karina Torres":
    three_data_gpt_predefinded += """
Prompt para un usuario de ChatGPT:
"¿Cuáles promociones hay actualmente disponibles para los productos de Coca-Cola?"
Respuesta de ChatGPT:
Las promociones actuales disponibles para los productos de Coca-Cola son:
Promoción 1:
Descripción: 5% menos a todos los productos de Santa Clara.
Promoción 2:
Descripción: Recibe seis latas Del Valle de 250ml por cada docena de Tetrapack Santa Clara de litro comprados.
Promoción 3:
Descripción: Combo de 12 Tetrapack Del Valle de 250ml y 3 Tetrapack Santa Clara de 200ml a $100.
Promoción 1:
5% menos a todos los productos de Santa Clara
Promoción 2:
Sies latas Del Valle de 250ml por cada docena de Tetrapack Santa Clara de litro.
Promoción 3:
Combo de 12 Tetrapack Del Valle de 250ml y 3 Tetrapack Santa Clara de 200ml a $100
Estas promociones están diseñadas para ofrecer descuentos y beneficios adicionales al comprar productos específicos de la línea de bebidas de la familia Coca-Cola.
    """


four_data_gpt_predefinded = """
2848	DEL VALLE NARANJA 946 ML NR TPK 12	265.03	17.86	0.00	265.49
"""