from datetime import datetime
from marshmallow import Schema, fields, validates, ValidationError
import re
from enum import Enum

class GenderEnum(Enum):
    FEMALE = "Female"
    MALE = "Male"
    OTHER = "Other"

class GenderEnum(Enum):
    FEMALE = "Female"
    MALE = "Male"
    OTHER = "Other"

class CountryEnum(Enum):
    AFGHANISTAN = "Afghanistan", "AF"
    ALAND_ISLANDS = "Aland Islands", "AX"
    ALBANIA = "Albania", "AL"
    ALGERIA = "Algeria", "DZ"
    AMERICAN_SAMOA = "American Samoa", "AS"
    ANDORRA = "Andorra", "AD"
    ANGOLA = "Angola", "AO"
    ANGUILLA = "Anguilla", "AI"
    ANTARCTICA = "Antarctica", "AQ"
    ANTIGUA_AND_BARBUDA = "Antigua and Barbuda", "AG"
    ARGENTINA = "Argentina", "AR"
    ARMENIA = "Armenia", "AM"
    ARUBA = "Aruba", "AW"
    AUSTRALIA = "Australia", "AU"
    AUSTRIA = "Austria", "AT"
    AZERBAIJAN = "Azerbaijan", "AZ"
    BAHAMAS = "Bahamas", "BS"
    BAHRAIN = "Bahrain", "BH"
    BANGLADESH = "Bangladesh", "BD"
    BARBADOS = "Barbados", "BB"
    BELARUS = "Belarus", "BY"
    BELGIUM = "Belgium", "BE"
    BELIZE = "Belize", "BZ"
    BENIN = "Benin", "BJ"
    BERMUDA = "Bermuda", "BM"
    BHUTAN = "Bhutan", "BT"
    BOLIVIA = "Bolivia", "BO"
    BONAIRE = "Bonaire", "BQ"
    BOSNIA_AND_HERZEGOVINA = "Bosnia and Herzegovina", "BA"
    BOTSWANA = "Botswana", "BW"
    BOUVET_ISLAND = "Bouvet Island", "BV"
    BRAZIL = "Brazil", "BR"
    BRITISH_INDIAN_OCEAN_TERRITORY = "British Indian Ocean Territory", "IO"
    BRUNEI_DARUSSALAM = "Brunéi Darussalam", "BN"
    BULGARIA = "Bulgaria", "BG"
    BURKINA_FASO = "Burkina Faso", "BF"
    BURUNDI = "Burundi", "BI"
    CABO_VERDE = "Cabo Verde", "CV"
    CAMBODIA = "Cambodia", "KH"
    CAMEROON = "Cameroon", "CM"
    CANADA = "Canada", "CA"
    CAYMAN_ISLANDS = "Cayman Islands", "KY"
    CENTRAL_AFRICAN_REPUBLIC = "Central African Republic", "CF"
    CHAD = "Chad", "TD"
    CHILE = "Chile", "CL"
    CHINA = "China", "CN"
    CHRISTMAS_ISLAND = "Christmas Island", "CX"
    COCOS_KEELING_ISLANDS = "Cocos (Keeling) Islands", "CC"
    COLOMBIA = "Colombia", "CO"
    COMOROS = "Comoros", "KM"
    CONGO = "Congo", "CG"
    CONGO_THE_DEMOCRATIC_REPUBLIC_OF_THE = "Congo, the Democratic Republic of the", "CD"
    COOK_ISLANDS = "Cook Islands", "CK"
    COSTA_RICA = "Costa Rica", "CR"
    COTE_D_IVOIRE = "Cote D'Ivoire", "CI"
    CROATIA = "Croatia", "HR"
    CUBA = "Cuba", "CU"
    CURACAO = "Curacao", "CW"
    CYPRUS = "Cyprus", "CY"
    CZECHIA = "Czechia", "CZ"
    DENMARK = "Denmark", "DK"
    DJIBOUTI = "Djibouti", "DJ"
    DOMINICA = "Dominica", "DM"
    DOMINICAN_REPUBLIC = "Dominican Republic", "DO"
    ECUADOR = "Ecuador", "EC"
    EGYPT = "Egypt", "EG"
    EL_SALVADOR = "El Salvador", "SV"
    EQUATORIAL_GUINEA = "Equatorial Guinea", "GQ"
    ERITREA = "Eritrea", "ER"
    ESTONIA = "Estonia", "EE"
    ESWATINI = "Eswatini", "SZ"
    ETHIOPIA = "Ethiopia", "ET"
    FALKLAND_ISLANDS_MALVINAS = "Falkland Islands (Malvinas)", "FK"
    FAROE_ISLANDS = "Faroe Islands", "FO"
    FIJI = "Fiji", "FJ"
    FINLAND = "Finland", "FI"
    FRANCE = "France", "FR"
    FRENCH_GUIANA = "French Guiana", "GF"
    FRENCH_POLYNESIA = "French Polynesia", "PF"
    FRENCH_SOUTHERN_TERRITORIES = "French Southern Territories", "TF"
    GABON = "Gabon", "GA"
    GAMBIA = "Gambia", "GM"
    GEORGIA = "Georgia", "GE"
    GERMANY = "Germany", "DE"
    GHANA = "Ghana", "GH"
    GIBRALTAR = "Gibraltar", "GI"
    GREECE = "Greece", "GR"
    GREENLAND = "Greenland", "GL"
    GRENADA = "Grenada", "GD"
    GUADELOUPE = "Guadeloupe", "GP"
    GUAM = "Guam", "GU"
    GUATEMALA = "Guatemala", "GT"
    GUERNSEY = "Guernsey", "GG"
    GUINEA = "Guinea", "GN"
    GUINEA_BISSAU = "Guinea-Bissau", "GW"
    GUYANA = "Guyana", "GY"
    HAITI = "Haiti", "HT"
    HEARD_ISLAND_MCDONALD_ISLANDS = "Heard Island and Mcdonald Islands", "HM"
    HOLY_SEE = "Holy See", "VA"
    HONDURAS = "Honduras", "HN"
    HONG_KONG = "Hong Kong", "HK"
    HUNGARY = "Hungary", "HU"
    ICELAND = "Iceland", "IS"
    INDIA = "India", "IN"
    INDONESIA = "Indonesia", "ID"
    IRAN_ISLAMIC_REPUBLIC_OF = "Iran Islamic Republic of", "IR"
    IRAQ = "Iraq", "IQ"
    IRELAND = "Ireland", "IE"
    ISLE_OF_MAN = "Isle of Man", "IM"
    ISRAEL = "Israel", "IL"
    ITALY = "Italy", "IT"
    JAMAICA = "Jamaica", "JM"
    JAPAN = "Japan", "JP"
    JERSEY = "Jersey", "JE"
    JORDAN = "Jordan", "JO"
    KAZAKHSTAN = "Kazakhstan", "KZ"
    KENYA = "Kenya", "KE"
    KIRIBATI = "Kiribati", "KI"
    KOREA = "Korea", "KP"
    KUWAIT = "Kuwait", "KW"
    KYRGYZSTAN = "Kyrgyzstan", "KG"
    LAO_PEOPLES_DEMOCRATIC_REPUBLIC = "Lao People's Democratic Republic", "LA"
    LATVIA = "Latvia", "LV"
    LEBANON = "Lebanon", "LB"
    LESOTHO = "Lesotho", "LS"
    LIBERIA = "Liberia", "LR"
    LIBYA = "Libya", "LY"
    LIECHTENSTEIN = "Liechtenstein", "LI"
    LITHUANIA = "Lithuania", "LT"
    LUXEMBOURG = "Luxembourg", "LU"
    MACAO = "Macao", "MO"
    MADAGASCAR = "Madagascar", "MG"
    MALAWI = "Malawi", "MW"
    MALAYSIA = "Malaysia", "MY"
    MALDIVES = "Maldives", "MV"
    MALI = "Mali", "ML"
    MALTA = "Malta", "MT"
    MARSHALL_ISLANDS = "Marshall Islands", "MH"
    MARTINIQUE = "Martinique", "MQ"
    MAURITANIA = "Mauritania", "MR"
    MAURITIUS = "Mauritius", "MU"
    MAYOTTE = "Mayotte", "YT"
    MEXICO = "Mexico", "MX"
    MICRONESIA = "Micronesia", "FM"
    MOLDOVA = "Moldova", "MD"
    MONACO = "Monaco", "MC"
    MONGOLIA = "Mongolia", "MN"
    MONTENEGRO = "Montenegro", "ME"
    MONTSERRAT = "Montserrat", "MS"
    MOROCCO = "Morocco", "MA"
    MOZAMBIQUE = "Mozambique", "MZ"
    MYANMAR = "Myanmar", "MM"
    NAMIBIA = "Namibia", "NA"
    NAURU = "Nauru", "NR"
    NEPAL = "Nepal", "NP"
    NETHERLANDS = "Netherlands", "NL"
    NEW_CALEDONIA = "New Caledonia", "NC"
    NEW_ZEALAND = "New Zealand", "NZ"
    NICARAGUA = "Nicaragua", "NI"
    NIGER = "Niger", "NE"
    NIGERIA = "Nigeria", "NG"
    NIUE = "Niue", "NU"
    NORFOLK_ISLAND = "Norfolk Island", "NF"
    NORTH_MACEDONIA = "North Macedonia", "MK"
    NORTHERN_MARIANA_ISLANDS = "Northern Mariana Islands", "MP"
    NORWAY = "Norway", "NO"
    OMAN = "Oman", "OM"
    PAKISTAN = "Pakistan", "PK"
    PALAU = "Palau", "PW"
    PALESTINE = "Palestine", "PS"
    PANAMA = "Panama", "PA"
    PAPUA_NEW_GUINEA = "Papua New Guinea", "PG"
    PARAGUAY = "Paraguay", "PY"
    PERU = "Peru", "PE"
    PHILIPPINES = "Philippines", "PH"
    PITCAIRN = "Pitcairn", "PN"
    POLAND = "Poland", "PL"
    PORTUGAL = "Portugal", "PT"
    PUERTO_RICO = "Puerto Rico", "PR"
    QATAR = "Qatar", "QA"
    REUNION = "Reunion", "RE"
    ROMANIA = "Romania", "RO"
    RUSSIA = "Russia", "RU"
    RWANDA = "Rwanda", "RW"
    SAINT_BARTHELEMY = "Saint Barthelemy", "BL"
    SAINT_HELENA = "Saint Helena", "SH"
    SAINT_KITTS_AND_NEVIS = "Saint Kitts and Nevis", "KN"
    SAINT_LUCIA = "Saint Lucia", "LC"
    SAINT_MARTIN = "Saint Martin", "MF"
    SAINT_PIERRE_AND_MIQUELON = "Saint Pierre and Miquelon", "PM"
    SAINT_VINCENT_AND_THE_GRENADINES = "Saint Vincent and the Grenadines", "VC"
    SAMOA = "Samoa", "WS"
    SAN_MARINO = "San Marino", "SM"
    SAO_TOME_AND_PRINCIPE = "Sao Tome and Principe", "ST"
    SAUDI_ARABIA = "Saudi Arabia", "SA"
    SENEGAL = "Senegal", "SN"
    SERBIA = "Serbia", "RS"
    SEYCHELLES = "Seychelles", "SC"
    SIERRA_LEONE = "Sierra Leone", "SL"
    SINGAPORE = "Singapore", "SG"
    SINT_MAARTEN = "Sint Maarten", "SX"
    SLOVAKIA = "Slovakia", "SK"
    SLOVENIA = "Slovenia", "SI"
    SOLOMON_ISLANDS = "Solomon Islands", "SB"
    SOMALIA = "Somalia", "SO"
    SOUTH_AFRICA = "South Africa", "ZA"
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = "South Georgia and the South Sandwich Islands", "GS"
    SOUTH_SUDAN = "South Sudan", "SS"
    SPAIN = "Spain", "ES"
    SRI_LANKA = "Sri Lanka", "LK"
    SUDAN = "Sudan", "SD"
    SURINAME = "Suriname", "SR"
    SVALBARD_AND_JAN_MAYEN = "Svalbard and Jan Mayen", "SJ"
    SWEDEN = "Sweden", "SE"
    SWITZERLAND = "Switzerland", "CH"
    SYRIAN_ARAB_REPUBLIC = "Syrian Arab Republic", "SY"
    TAIWAN = "Taiwan", "TW"
    TAJIKISTAN = "Tajikistan", "TJ"
    TANZANIA = "Tanzania", "TZ"
    THAILAND = "Thailand", "TH"
    TIMOR_LESTE = "Timor-Leste", "TL"
    TOGO = "Togo", "TG"
    TOKELAU = "Tokelau", "TK"
    TONGA = "Tonga", "TO"
    TRINIDAD_AND_TOBAGO = "Trinidad and Tobago", "TT"
    TUNISIA = "Tunisia", "TN"
    TURKEY = "Turkey", "TR"
    TURKMENISTAN = "Turkmenistan", "TM"
    TURKS_AND_CAICOS_ISLANDS = "Turks and Caicos Islands", "TC"
    TUVALU = "Tuvalu", "TV"
    UGANDA = "Uganda", "UG"
    UKRAINE = "Ukraine", "UA"
    UNITED_ARAB_EMIRATES = "United Arab Emirates", "AE"
    UNITED_KINGDOM_OF_GREAT_BRITAIN_AND_NORTHERN_IRELAND = "United Kingdom of Great Britain and Northern Ireland", "GB"
    UNITED_STATES_OF_AMERICA = "United States of America", "US"
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = "United States Minor Outlying Islands", "UM"
    URUGUAY = "Uruguay", "UY"
    UZBEKISTAN = "Uzbekistan", "UZ"
    VANUATU = "Vanuatu", "VU"
    VENEZUELA = "Venezuela", "VE"
    VIETNAM = "Vietnam", "VN"
    VIRGIN_ISLANDS_BRITISH = "Virgin Islands (British)", "VG"
    VIRGIN_ISLANDS_US = "Virgin Islands (U.S.)", "VI"
    WALLIS_AND_FUTUNA_ISLANDS = "Wallis and Futuna Islands", "WF"
    WESTERN_SAHARA = "Western Sahara", "EH"
    YEMEN = "Yemen", "YE"
    ZAMBIA = "Zambia", "ZM"
    ZIMBABWE = "Zimbabwe", "ZW"

class LanguageEnum(Enum):
    Afar = "AA"
    Abkhazian = "AB"
    Afrikaans = "AF"
    Akan = "AK"
    Albanian = "SQ"
    Amharic = "AM"
    Arabic = "AR"
    Aragonese = "AN"
    Armenian = "HY"
    Assamese = "AS"
    Avaric = "AV"
    Avestan = "AE"
    Aymara = "AY"
    Azerbaijani = "AZ"
    Bambara = "BM"
    Bashkir = "BA"
    Basque = "EU"
    Belarusian = "BE"
    Bengali = "BN"
    Bihari = "BH"
    Bislama = "BI"
    Bosnian = "BS"
    Breton = "BR"
    Bulgarian = "BG"
    Burmese = "MY"
    Catalan = "CA"
    CentralKhmer = "KM"
    Chamorro = "CH"
    Chechen = "CE"
    Chichewa = "NY"
    Chinese = "ZH"
    ChurchSlavic = "CU"
    Chuvash = "CV"
    Cornish = "KW"
    Corsican = "CO"
    Cree = "CR"
    Croatian = "HR"
    Czech = "CS"
    Danish = "DA"
    Divehi = "DV"
    Dutch = "NL"
    Dzongkha = "DZ"
    English = "EN"
    Esperanto = "EO"
    Estonian = "ET"
    Ewe = "EE"
    Faroese = "FO"
    Fijian = "FJ"
    Finnish = "FI"
    French = "FR"
    Fulah = "FF"
    Galician = "GL"
    Georgian = "KA"
    German = "DE"
    Greek = "EL"
    Guarani = "GN"
    Gujarati = "GU"
    Haitian = "HT"
    Hausa = "HA"
    Hebrew = "HE"
    Herero = "HZ"
    Hindi = "HI"
    HiriMotu = "HO"
    Hungarian = "HU"
    Interlingua = "IA"
    Indonesian = "ID"
    Interlingue = "IE"
    Irish = "GA"
    Igbo = "IG"
    Inupiaq = "IK"
    Icelandic = "IS"
    Italian = "IT"
    Inuktitut = "IU"
    Japanese = "JA"
    Javanese = "JV"
    Kalaallisut = "KL"
    Kannada = "KN"
    Kanuri = "KR"
    Kashmiri = "KS"
    Kazakh = "KK"
    Kikuyu = "KI"
    Kinyarwanda = "RW"
    Kirghiz = "KY"
    Komi = "KV"
    Kongo = "KG"
    Korean = "KO"
    Kurdish = "KU"
    Kuanyama = "KJ"
    Latin = "LA"
    Luxembourgish = "LB"
    Ganda = "LG"
    Limburgan = "LI"
    Lingala = "LN"
    Lao = "LO"
    Lithuanian = "LT"
    LubaKatanga = "LU"
    Latvian = "LV"
    Manx = "GV"
    Macedonian = "MK"
    Malagasy = "MG"
    Malay = "MS"
    Malayalam = "ML"
    Maltese = "MT"
    Maori = "MI"
    Marathi = "MR"
    Marshallese = "MH"
    Mongolian = "MN"
    Nauru = "NA"
    Navajo = "NV"
    NorthNdebele = "ND"
    Nepali = "NE"
    Ndonga = "NG"
    NorwegianBokmal = "NB"
    NorwegianNynorsk = "NN"
    Norwegian = "NO"
    SichuanYi = "II"
    SouthNdebele = "NR"
    Occitan = "OC"
    Ojibwa = "OJ"
    ChurchSlavic = "CU"
    Oromo = "OM"
    Oriya = "OR"
    Ossetian = "OS"
    Punjabi = "PA"
    Pali = "PI"
    Polish = "PL"
    Pashto = "PS"
    Portuguese = "PT"
    Quechua = "QU"
    Reunionese = "RC"
    Romanian = "RO"
    Romansh = "RM"
    Rundi = "RN"
    Russian = "RU"
    Sango = "SG"
    Sanskrit = "SA"
    Sinhala = "SI"
    Slovak = "SK"
    Slovenian = "SL"
    NorthernSami = "SE"
    Samoan = "SM"
    Shona = "SN"
    Sindhi = "SD"
    Somali = "SO"
    Sotho = "ST"
    Spanish = "ES"
    Sardinian = "SC"
    Serbian = "SR"
    Swati = "SS"
    Sundanese = "SU"
    Swahili = "SW"
    Swedish = "SV"
    Tahitian = "TY"
    Tamil = "TA"
    Tatar = "TT"
    Telugu = "TE"
    Tajik = "TG"
    Tagalog = "TL"
    Thai = "TH"
    Tibetan = "BO"
    Tigrinya = "TI"
    Tonga = "TO"
    Tswana = "TN"
    Tsonga = "TS"
    Turkmen = "TK"
    Turkish = "TR"
    Twi = "TW"
    Uighur = "UG"
    Ukrainian = "UK"
    Urdu = "UR"
    Uzbek = "UZ"
    Venda = "VE"
    Vietnamese = "VI"
    Volapuk = "VO"
    Walloon = "WA"
    Welsh = "CY"
    Wolof = "WO"
    WesternFrisian = "FY"
    Xhosa = "XH"
    Yiddish = "YI"
    Yoruba = "YO"
    Zhuang = "ZA"
    Zulu = "ZU"

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email(required=True)
    registrationDate = fields.DateTime(required=True)
    profilePic = fields.Url(required=False)
    firstName = fields.String(required=True)
    lastName = fields.String(required=True)
    birthdate = fields.DateTime(required=False)
    gender = fields.String(required=False, validate=fields.validate.OneOf([gender.value for gender in GenderEnum]))
    pronouns = fields.String(required=False)
    country = fields.String(required=False, validate=fields.validate.OneOf([country.value for country in CountryEnum]))
    language = fields.String(required=False, validate=fields.validate.OneOf([language.value for language in LanguageEnum]))
    about = fields.String(required=False)
    websiteURL = fields.Url(required=False)
    isDeactivated = fields.Boolean(required=False, default=False)
    isDeleted = fields.Boolean(required=False, default=False)

    @validates("password")
    def validate_password(self, password: str):
        if len(password) < 8:
            raise ValidationError("Password should be at least 8 characters long.")

        special_character_regex = r"\W"
        if not re.search(special_character_regex, password):
            raise ValidationError("Password should contain at least one special character.")

        if not any(char.isupper() for char in password):
            raise ValidationError("Password should contain at least one uppercase letter.")

        if not any(char.islower() for char in password):
            raise ValidationError("Password should contain at least one lowercase letter.")

        if not any(char.isdigit() for char in password):
            raise ValidationError("Password should contain at least one digit.")
        
    @validates("birthdate")
    def validate_birthdate(self, birthdate: datetime):
        if birthdate >= datetime.now():
            raise ValidationError("Birthdate must be in the past.")
        if (datetime.now() - self.context.get('birthdate')).days < 16 * 365:
            raise ValidationError("You have to be 16 or older.") 