# fileName : plugins/dm/callBack/asImgOrDoc.py
# copyright ÂŠī¸ 2021 nabilanavab




from pyrogram import filters
from pyrogram import Client as ILovePDF
from plugins.fileSize import get_size_format as gSF
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup




#--------------->
#--------> LOCAL VARIABLES
#------------------->

pdfReply = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "â­ get page No & info â­",
                    callback_data="pdfInfo"
                )
            ],
            [
                InlineKeyboardButton(
                    "To Images đŧī¸",
                    callback_data="toImage"
                ),
                InlineKeyboardButton(
                    "To Text âī¸",
                    callback_data="toText"
                )
            ],
            [
                InlineKeyboardButton(
                    "Encrypt đ",
                    callback_data="encrypt"
                ),
                InlineKeyboardButton(
                    "Decrypt đ",
                    callback_data="decrypt"
                )
            ],
            [
                InlineKeyboardButton(
                    "Compress đī¸",
                    callback_data="compress"
                ),
                InlineKeyboardButton(
                    "Rotate đ¤¸",
                    callback_data="rotate"
                )
            ],
            [
                InlineKeyboardButton(
                    "Split âī¸",
                    callback_data="split"
                ),
                InlineKeyboardButton(
                    "Merge đ§Ŧ",
                    callback_data="merge"
                )
            ],
            [
                InlineKeyboardButton(
                    "Stamp âĸī¸",
                    callback_data="stamp"
                ),
                InlineKeyboardButton(
                    "Rename âī¸",
                    callback_data="rename"
                )
            ]
        ]
    )


BTPMcb = """`What shall i wanted to do with this file.?`

File Name: `{}`
File Size: `{}`"""


KBTPMcb = """`What shall i wanted to do with this file.?`

File Name: `{}`
File Size: `{}`

`Number of Pages: {}`âī¸"""

#--------------->
#--------> LOCAL VARIABLES
#------------------->

"""
______VARIABLES______

I : as image
D : as document
K : pgNo known
A : Extract All
R : Extract Range
S : Extract Single page
BTPM : back to pdf message
KBTPM : back to pdf message (known pages)

"""

#--------------->
#--------> PDF TO IMAGES (CB/BUTTON)
#------------------->


BTPM = filters.create(lambda _, __, query: query.data == "BTPM")
toImage = filters.create(lambda _, __, query: query.data == "toImage")
KBTPM = filters.create(lambda _, __, query: query.data.startswith("KBTPM|"))
KtoImage = filters.create(lambda _, __, query: query.data.startswith("KtoImage|"))

I = filters.create(lambda _, __, query: query.data == "I")
D = filters.create(lambda _, __, query: query.data == "D")
KI = filters.create(lambda _, __, query: query.data.startswith("KI|"))
KD = filters.create(lambda _, __, query: query.data.startswith("KD|"))


# Extract pgNo (with unknown pdf page number)
@ILovePDF.on_callback_query(I)
async def _I(bot, callbackQuery):
    try:
        await callbackQuery.edit_message_text(
            "__Pdf - Img Âģ as Img Âģ Pages:           \nTotal pages: unknown__ đ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Extract All đ",
                            callback_data="IA"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "With In Range đ",
                            callback_data="IR"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Single Page đ",
                            callback_data="IS"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "ÂĢ Back ÂĢ",
                            callback_data="toImage"
                        )
                    ]
                ]
            )
        )
    except Exception:
        pass


# Extract pgNo (with unknown pdf page number)
@ILovePDF.on_callback_query(D)
async def _D(bot, callbackQuery):
    try:
        await callbackQuery.edit_message_text(
            "__Pdf - Img Âģ as Doc Âģ Pages:           \nTotal pages: unknown__ đ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Extract All đ",
                            callback_data="DA"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "With In Range đ",
                            callback_data="DR"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Single Page đ",
                            callback_data="DS"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "ÂĢ Back ÂĢ",
                            callback_data="toImage"
                        )
                    ]
                ]
            )
        )
    except Exception:
        pass


# Extract pgNo (with known pdf page number)
@ILovePDF.on_callback_query(KI)
async def _KI(bot, callbackQuery):
    try:
        _, number_of_pages = callbackQuery.data.split("|")
        await callbackQuery.edit_message_text(
            f"__Pdf - Img Âģ as Img Âģ Pages:           \nTotal pages: {number_of_pages}__ đ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Extract All đ",
                            callback_data=f"KIA|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "With In Range đ",
                            callback_data=f"KIR|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Single Page đ",
                            callback_data=f"KIS|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "ÂĢ Back ÂĢ",
                            callback_data=f"KtoImage|{number_of_pages}"
                        )
                    ]
                ]
            )
        )
    except Exception:
        pass


# Extract pgNo (with known pdf page number)
@ILovePDF.on_callback_query(KD)
async def _KD(bot, callbackQuery):
    try:
        _, number_of_pages = callbackQuery.data.split("|")
        await callbackQuery.edit_message_text(
            f"__Pdf - Img Âģ as Doc Âģ Pages:           \nTotal pages: {number_of_pages}__ đ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Extract All đ",
                            callback_data=f"KDA|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "With In Range đ",
                            callback_data=f"KDR|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Single Page đ",
                            callback_data=f"KDS|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "ÂĢ Back ÂĢ",
                            callback_data=f"KtoImage|{number_of_pages}"
                        )
                    ]
                ]
            )
        )
    except Exception:
        pass

# pdf to images (with unknown pdf page number)
@ILovePDF.on_callback_query(toImage)
async def _toImage(bot, callbackQuery):
    try:
        await callbackQuery.edit_message_text(
            "__Send pdf Images as:           \nTotal pages: unknown__ đ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Images đŧī¸",
                            callback_data="I"
                        ),
                        InlineKeyboardButton(
                            "Documents đ",
                            callback_data="D"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "ÂĢ Back ÂĢ",
                            callback_data="BTPM"
                        )
                    ]
                ]
            )
        )
    except Exception:
        pass


# pdf to images (with known page Number)
@ILovePDF.on_callback_query(KtoImage)
async def _KtoImage(bot, callbackQuery):
    try:
        _, number_of_pages = callbackQuery.data.split("|")
        await callbackQuery.edit_message_text(
            f"__Send pdf Images as:           \nTotal pages: {number_of_pages}__ đ",
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Images đŧī¸",
                            callback_data=f"KI|{number_of_pages}"
                        ),
                        InlineKeyboardButton(
                            "Documents đ",
                            callback_data=f"KD|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "ÂĢBack ÂĢ",
                            callback_data=f"KBTPM|{number_of_pages}"
                        )
                    ]
                ]
            )
        )
    except Exception:
        pass


# back to pdf message (unknown page number)
@ILovePDF.on_callback_query(BTPM)
async def _BTPM(bot, callbackQuery):
    try:
        fileName=callbackQuery.message.reply_to_message.document.file_name
        fileSize=callbackQuery.message.reply_to_message.document.file_size
        
        await callbackQuery.edit_message_text(
            BTPMcb.format(
                fileName, await gSF(fileSize)
            ),
            reply_markup = pdfReply
        )
    except Exception:
        pass


# back to pdf message (with known page Number)
@ILovePDF.on_callback_query(KBTPM)
async def _KBTPM(bot, callbackQuery):
    try:
        fileName = callbackQuery.message.reply_to_message.document.file_name
        fileSize = callbackQuery.message.reply_to_message.document.file_size
        
        _, number_of_pages = callbackQuery.data.split("|")
        await callbackQuery.edit_message_text(
            KBTPMcb.format(
                fileName, await gSF(fileSize), number_of_pages
            ),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "â­get page No & infoâ­",
                            callback_data=f"KpdfInfo|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "To Images đŧī¸",
                            callback_data=f"KtoImage|{number_of_pages}"
                        ),
                        InlineKeyboardButton(
                            "To Text âī¸",
                            callback_data=f"KtoText|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Encrypt đ",
                            callback_data=f"Kencrypt|{number_of_pages}"
                        ),
                        InlineKeyboardButton(
                            "Decrypt đ",
                            callback_data=f"notEncrypted"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Compress đī¸",
                            callback_data=f"Kcompress"
                        ),
                        InlineKeyboardButton(
                            "Rotate đ¤¸",
                            callback_data=f"Krotate|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Split âī¸",
                            callback_data=f"Ksplit|{number_of_pages}"
                        ),
                        InlineKeyboardButton(
                            "Merge đ§Ŧ",
                            callback_data="merge"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Stamp âĸī¸",
                            callback_data=f"Kstamp|{number_of_pages}"
                        ),
                        InlineKeyboardButton(
                            "Rename",
                            callback_data="rename"
                        )
                    ]
                ]
            )
        )
    except Exception:
        pass


#                                                                                  Telegram: @nabilanavab
