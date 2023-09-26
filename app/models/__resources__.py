from dataclasses import dataclass
from pprint import pprint


@dataclass
class Resources:
    roles = [
        {"name": "Super Administrator"},
        {"name": "Administrator"},
        {"name": "Conference Chair"},
        {"name": "Grants Chair"},
        {"name": "Volunteer Chair"},
        {"name": "Sprints Chair"},
        {"name": "Speaker Support Chair"},
        {"name": "Sponsorship Chair"},
        {"name": "Diversity Chair"},
        {"name": "Code of Conduct Official"},
        {"name": "Proposal Reviewer"},
        {"name": "Speaker"},
        {"name": "Volunteer"},
        {"name": "VIP"},
        {"name": "Attendee"},
        {"name": "Emeritus"},
    ]

    sponsor_levels = [
        {"name": "Platinum"},
        {"name": "Gold"},
        {"name": "Silver"},
        {"name": "Bronze"},
        {"name": "Donor"},
    ]

    talk_statuses = [
        {
            "name": "Preparation",
            "description": "Not yet submitted, but saved for safe keeping.",
            "unique_talk_status_id": 101
        },
        {
            "name": "Proposal",
            "description": "Your talk has been submitted.",
            "unique_talk_status_id": 102
        },
        {
            "name": "Under Review",
            "description": "Your talk is being reviewed by the committee.",
            "unique_talk_status_id": 103
        },
        {
            "name": "Change Requested",
            "description": "The committee has requested changes to your talk.",
            "unique_talk_status_id": 104
        },
        {
            "name": "Changes Made",
            "description": "You have made the requested changes to your talk.",
            "unique_talk_status_id": 105
        },
        {
            "name": "Waitlisted",
            "description": "Your talk was not accepted, but may be accepted if another talk is cancelled.",
            "unique_talk_status_id": 106
        },
        {
            "name": "Accepted",
            "description": "Your talk has been accepted.",
            "unique_talk_status_id": 107
        },
        {
            "name": "Rejected",
            "description": "Your talk has been rejected.",
            "unique_talk_status_id": 108
        },
        {
            "name": "Cancelled",
            "description": "You have cancelled your talk.",
            "unique_talk_status_id": 109
        },
    ]

    original_display_pictures = [
        {'attribution': 'Tom Dils',
         'attribution_url': 'https://unsplash.com/@tdils',
         'filename': 'ogdp1.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 1},
        {'attribution': 'Sandy Millar',
         'attribution_url': 'https://unsplash.com/@sandym10',
         'filename': 'ogdp2.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 2},
        {'attribution': 'Ricky Kharawala',
         'attribution_url': 'https://unsplash.com/@sweetmangostudios',
         'filename': 'ogdp3.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 3},
        {'attribution': 'Richard Brutyo',
         'attribution_url': 'https://unsplash.com/@richardbrutyo',
         'filename': 'ogdp4.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 4},
        {'attribution': 'Piotr Łaskawski',
         'attribution_url': 'https://unsplash.com/@tot87',
         'filename': 'ogdp5.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 5},
        {'attribution': 'Nathan Anderson',
         'attribution_url': 'https://unsplash.com/@nathananderson',
         'filename': 'ogdp6.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 6},
        {'attribution': 'Matthew Henry',
         'attribution_url': 'https://unsplash.com/@matthewhenry',
         'filename': 'ogdp7.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 7},
        {'attribution': 'Jamie Haughton',
         'attribution_url': 'https://unsplash.com/@haughters',
         'filename': 'ogdp8.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 8},
        {'attribution': 'Geranimo',
         'attribution_url': 'https://unsplash.com/@geraninmo',
         'filename': 'ogdp9.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 9},
        {'attribution': 'Gary Bendig',
         'attribution_url': 'https://unsplash.com/@kris_ricepees',
         'filename': 'ogdp10.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 10},
        {'attribution': 'Francesco',
         'attribution_url': 'https://unsplash.com/@detpho',
         'filename': 'ogdp11.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 11},
        {'attribution': 'Edgar',
         'attribution_url': 'https://unsplash.com/@e_d_g_a_r',
         'filename': 'ogdp12.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 12},
        {'attribution': 'David Clode',
         'attribution_url': 'https://unsplash.com/@davidclode',
         'filename': 'ogdp14.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 14},
        {'attribution': 'Cristina Anne Costello',
         'attribution_url': 'https://unsplash.com/@lightupphotos',
         'filename': 'ogdp15.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 15},
        {'attribution': 'Christopher Carson',
         'attribution_url': 'https://unsplash.com/@bhris1017',
         'filename': 'ogdp16.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 16},
        {'attribution': 'Chris Curry',
         'attribution_url': 'https://unsplash.com/@chriscurry92',
         'filename': 'ogdp17.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 17},
        {'attribution': 'Charles Deluvio',
         'attribution_url': 'https://unsplash.com/@charlesdeluvio',
         'filename': 'ogdp18.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 18},
        {'attribution': 'Robert Woeger',
         'attribution_url': 'https://unsplash.com/@woeger',
         'filename': 'ogdp19.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 19},
        {'attribution': 'Andriyko Podilnyk',
         'attribution_url': 'https://unsplash.com/@andriyko',
         'filename': 'ogdp20.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 20},
        {'attribution': 'Ádám Berkecz',
         'attribution_url': 'https://unsplash.com/@aberkecz',
         'filename': 'ogdp21.png',
         'limited': False,
         'note': 'Part of the standard display pictures for FlaskCon.',
         'unique_display_picture_id': 21},
        {'attribution': 'David Carmichael',
         'attribution_url': 'https://github.com/CheeseCake87',
         'filename': 'flaskcon2023.gif',
         'limited': True,
         'note': 'Awarded when you accessed your account during FlaskCon 2023.',
         'unique_display_picture_id': 2023}
    ]


if __name__ == '__main__':
    sorted_display_pictures = sorted(Resources.original_display_pictures, key=lambda x: x['unique_display_picture_id'])
    pprint(sorted_display_pictures)
