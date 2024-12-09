import os

os.environ.setdefault(
    "DATABASE_URL",
    "postgresql://neondb_owner:l13uWGsyePbM@ep-icy-fog-a2fhowul.eu-central-1.aws.neon.tech/romp_vegan_hut_429921"
)

# Django Secret Key
os.environ.setdefault(
    "SECRET_KEY",
    "a*&ow-#$tgb#@loi#+yblghqs&fi)stxwy)i9_2ib=bq#64&w"
)

# Cloudinary URL
os.environ.setdefault(
    "CLOUDINARY_URL",
    "cloudinary://486843237889555:Inv14d3b7cNt1noeSm_zQB6pl2I@dpj5ircwd"
)

# Ignore environment files
