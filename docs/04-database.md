# Safar Hazara: Database design

## destinations

Har row ek jagah hai (jaise Naran). Har column us jagah ki ek maloomat.

| Column | Type | Matlab |
|---|---|---|
| id | integer | Har destination ka alag number (primary key). Doosre tables isi se jurte hain. |
| name | text | Jagah ka naam, jaise Naran. |
| slug | text | Address mein use hone wala chhota naam, jaise naran. |
| description | text | Jagah ka taaruf. |
| latitude | decimal | Map par jagah ka pehla number. |
| longitude | decimal | Map par jagah ka doosra number. |
| best_season | text | Kab jana behtar hai. |
| transport | text | Kaise pahunchein (jaise jeep zaroori hai ya nahi). |
| packing_tips | text | Kya saath rakhein (garam kapre wagaira). |
| local_tips | text | Local logon ki salaah. |
| image_url | text | Photo ka address. |
| created_at | timestamp | Kab add hua. |

## Faisla
Tips ko alag table mein nahi, ek hi column mein text ki tarah rakha. 4 hafte ke project ke liye simple rakha, zaroorat par baad mein alag table banayenge.
## hotels

Har row ek hotel hai. Har hotel kisi ek destination ka hota hai.

| Column | Type | Matlab |
|---|---|---|
| id | integer | Har hotel ka alag number (primary key). |
| destination_id | integer | Yeh hotel kis destination ka hai (foreign key, destinations ki id). |
| name | text | Hotel ka naam. |
| description | text | Hotel ka taaruf. |
| price_min | integer | Ek raat ka kam az kam kiraya (rupay mein). |
| price_max | integer | Ek raat ka zyada se zyada kiraya (rupay mein). |
| services | text | Kya sahulat hai (khana, garam pani, parking wagaira). |
| phone | text | Rabta number. |
| image_url | text | Photo ka address. |
| created_at | timestamp | Kab add hua. |

Kiraya ek number ke bajaye range (min aur max) rakha, kyunke hotels ke rate season aur kamre ke hisaab se badalte hain.

## users

Har row ek user hai (Tourist ya Admin).

| Column | Type | Matlab |
|---|---|---|
| id | integer | Har user ka alag number (primary key). |
| name | text | User ka naam. |
| email | text | Email, har user ki alag (unique). |
| password_hash | text | Password ka hash. Asli password kabhi save nahi hota. |
| role | text | tourist ya admin. |
| created_at | timestamp | Kab bana. |