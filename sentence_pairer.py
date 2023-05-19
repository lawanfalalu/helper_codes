import csv

paragraphs = """Nigeria (/naɪˈdʒɪəriə/ Listen ny-JEER-ee-ə),[a] officially the Federal Republic of Nigeria, is a country in West Africa. It is situated between the Sahel to the north and the Gulf of Guinea to the south in the Atlantic Ocean. It covers an area of 923,769 square kilometres (356,669 sq mi), and with a population of over 230 million, it is the most populous country in Africa, and the world's sixth-most populous country. Nigeria borders Niger in the north, Chad in the northeast, Cameroon in the east, and Benin in the west. Nigeria is a federal republic comprising 36 states and the Federal Capital Territory, where the capital, Abuja, is located. The largest city in Nigeria is Lagos, one of the largest metropolitan areas in the world and the second-largest in Africa.

Nigeria has been home to several indigenous pre-colonial states and kingdoms since the second millennium BC, with the Nok civilization in the 15th century BC marking the first internal unification in the country. The modern state originated with British colonialization in the 19th century, taking its present territorial shape with the merging of the Southern Nigeria Protectorate and Northern Nigeria Protectorate in 1914 by Lord Lugard. The British set up administrative and legal structures while practising indirect rule through traditional chiefdoms in the Nigeria region.[9] Nigeria became a formally independent federation on 1 October 1960. It experienced a civil war from 1967 to 1970, followed by a succession of military dictatorships and democratically elected civilian governments until achieving a stable democracy in the 1999 presidential election. The 2015 general election was the first time an incumbent president failed to be re-elected.[10]

Nigeria is a multinational state inhabited by more than 250 ethnic groups speaking 500 distinct languages, all identifying with a wide variety of cultures.[11][12][13] The three largest ethnic groups are the Hausa in the north, Yoruba in the west, and Igbo in the east, together constituting over 60% of the total population.[14] The official language is English, chosen to facilitate linguistic unity at the national level.[15] Nigeria's constitution ensures freedom of religion[16] and it is home to some of the world's largest Muslim and Christian populations.[17] Nigeria is divided roughly in half between Muslims, who live mostly in the north, and Christians, who live mostly in the south; indigenous religions, such as those native to the Igbo and Yoruba ethnicities, are in the minority.[18]

Nigeria is a regional power in Africa and a middle and emerging power in international affairs. Nigeria's economy is the largest in Africa, the 31st-largest in the world by nominal GDP, and 26th-largest by PPP. Nigeria is often referred to as the Giant of Africa owing to its large population and economy[19] and is considered to be an emerging market by the World Bank. However, the country ranks very low in the Human Development Index and remains one of the most corrupt nations in the world.[20][21] Nigeria is a founding member of the African Union and a member of many international organizations, including the United Nations, the Commonwealth of Nations, NAM,[22] the Economic Community of West African States, Organisation of Islamic Cooperation and OPEC. It is also a member of the informal MINT group of countries and is one of the Next Eleven economies.

Etymology
The name Nigeria was taken from the Niger River running through the country. This name was coined on 8 January 1897, by the British journalist Flora Shaw, who later married Frederick Lugard, a British colonial administrator. The neighbouring Republic of Niger takes its name from the same river. The origin of the name Niger, which originally applied to only the middle reaches of the Niger River, is uncertain. The word is likely an alteration of the Tuareg name egerew n-igerewen used by inhabitants along the middle reaches of the river around Timbuktu before 19th-century European colonialism.[23][24]

History
Main articles: History of Nigeria and Timeline of Nigerian history
Prehistory and ancient history (before 1500)
Further information: Early history of Nigeria and History of Nigeria before 1500

Nok sculpture, terracotta
Kainji Dam excavations showed ironworking by the 2nd century BC. The transition from Neolithic times to the Iron Age was accomplished without intermediate bronze production. Others believe or suggest the technology moved west from the Nile Valley, although the Iron Age in the Niger River valley and the forest region appears to predate the introduction of metallurgy in the upper savanna by more than 800 years.

The Nok civilization of Nigeria thrived between 1,500 BC and AD 200. It produced life-sized terracotta figures that are some of the earliest known sculptures in Sub-Saharan Africa[25][26][27][28][29] and smelted iron by about 550 BC and possibly a few centuries earlier.[30][31][32] Evidence of iron smelting has also been excavated at sites in the Nsukka region of southeast Nigeria: dating to 2000 BC at the site of Lejja[33] and to 750 BC and at the site of Opi.

The Kano Chronicle highlights an ancient history dating to around 999 AD of the Hausa Sahelian city-state of Kano, with other major Hausa cities (or Hausa Bakwai) of Daura, Hadeija, Kano, Katsina, Zazzau, Rano, and Gobir all having recorded histories dating back to the 10th century. With the spread of Islam from the 7th century AD, the area became known as Sudan or as Bilad Al Sudan (English: Land of the Blacks; Arabic: بلاد السودان). Since the populations were partially affiliated with the Arab Muslim culture of North Africa, they began trans-Saharan trade and were referred to by the Arabic speakers as Al-Sudan (meaning "The Blacks") as they were considered an extended part of the Muslim world. There are early historical references by medieval Arab and Muslim historians and geographers which refer to the Kanem-Bornu Empire as the region's major centre for Islamic civilization.

The Kingdom of Nri of the Igbo people consolidated in the 10th century and continued until it lost its sovereignty to the British in 1911.[34][35] Nri was ruled by the Eze Nri, and the city of Nri is considered to be the foundation of Igbo culture. Nri and Aguleri, where the Igbo creation myth originates, are in the territory of the Umeuri clan. Members of the clan trace their lineages back to the patriarchal king-figure Eri.[36] In West Africa, the oldest bronzes made using the lost wax process were from Igbo-Ukwu, a city under Nri influence.[34]

The Yoruba kingdoms of Ife and Oyo in southwestern Nigeria became prominent in the 12th[37][38] and 14th[39] centuries, respectively. The oldest signs of human settlement at Ife's current site date back to the 9th century,[37] and its material culture includes terracotta and bronze figures."""

sentence_bi_grams = []

def paragraphs_exploder(text):
    paragraphs = text.split("\n")
    for paragraph in paragraphs:
        sentences = paragraph.split(". ")  # split on period.   
        for i in range(len(sentences)-1):
            pairs = (sentences[i], sentences[i+1])
            sentence_bi_grams.append(pairs)
            
    return sentence_bi_grams


bi_grams = paragraphs_exploder(paragraphs)

with open('sentence_pairs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Left', 'Right'])
    writer.writerows(bi_grams)

print("Done")