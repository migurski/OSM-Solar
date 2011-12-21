#place-labels[zoom<8][population>=50000] name,
#place-labels[zoom=8][population>=15000] name,
#place-labels[zoom=9][population>=5000] name,
#place-labels[zoom=10][population>=1000] name,
#place-labels[zoom>=11][zoom<15][population>0] name,
#place-labels[zoom>=11][zoom<15][place=city] name,
#place-labels[zoom>=11][zoom<15][place=town] name,
#place-labels[zoom>=15][zoom<17] name
{
    text-fill: #586e75;
    text-halo-fill: #fdf6e3;
    text-halo-radius: 2;
    
    text-placement: point;
}

#place-labels[zoom<13] name
{
    text-size: 14;
    text-face-name: 'DejaVu Sans Condensed';
}

#place-labels[zoom<13][population>=35000] name
{
    text-size: 16;
    text-face-name: 'DejaVu Sans Condensed';
}

#place-labels[zoom<13][population>=100000] name
{
    text-size: 19;
    text-face-name: 'DejaVu Sans Condensed';
}

#place-labels[zoom>=13] name
{
    text-size: 14;
    text-face-name: 'DejaVu Sans Condensed Bold';
}

#place-labels[zoom>=13][population>=35000] name
{
    text-size: 19;
    text-face-name: 'DejaVu Sans Condensed Bold';
}

#place-labels[zoom>=13][population>=100000] name
{
    text-size: 22;
    text-face-name: 'DejaVu Sans Condensed Bold';
}


/*
 * Water and Park labels.
 */

#water-labels name
{
    text-fill: #268bd2;
}

#green-labels name
{
    text-fill: #859900;
}

.area-labels[zoom=11][sq_km>3.2768][sq_km<51200] name,
.area-labels[zoom=12][sq_km>0.8192][sq_km<25600] name,
.area-labels[zoom=13][sq_km>0.2048][sq_km<12800] name,
.area-labels[zoom=14][sq_km>0.0512][sq_km<6400] name,
.area-labels[zoom=15][sq_km>0.0128][sq_km<3200] name,
.area-labels[zoom=16][sq_km>0.0064][sq_km<1600] name,
.area-labels[zoom=17][sq_km>0.0032][sq_km<800] name,
.area-labels[zoom=18][sq_km>0.0016][sq_km<400] name,
.area-labels[zoom>=19][sq_km<200] name
{
    text-face-name: 'DejaVu Sans Condensed';

    text-halo-fill: #fdf6e3;
    text-halo-radius: 2;

    text-wrap-width: 96;
}

.area-labels[zoom<13] name
{
    text-size: 12;
}

.area-labels[zoom>=13] name
{
    text-size: 14;
}


/*
 * Road labels.
 */

#major-road-labels[zoom>=16][highway=motorway] name,
#major-road-labels[zoom>=12][highway=trunk] name,
#major-road-labels[zoom>=12][highway=primary] name,
#major-road-labels[zoom>=13][highway=secondary] name,
#minor-road-labels[zoom>=15][highway=tertiary] name,
#minor-road-labels[zoom>=16] name
{
    text-face-name: 'DejaVu Sans Condensed';
    text-fill: #586e75;
    
    text-placement: line;
    text-spacing: 384;
    text-max-char-angle-delta: 30;
    
    text-halo-fill: #fdf6e3;
    text-halo-radius: 2;
}

/*
 * Increase text size when zoomed in and there's more room for large labels.
 */

#major-road-labels[zoom<14] name,
#minor-road-labels[zoom<16] name
{
    text-size: 12;
}

#major-road-labels[zoom>=14] name,
#minor-road-labels[zoom>=16] name
{
    text-size: 14;
}

/*
 * Switch to an outlined labels when roads are think enough to match them.
 */

#major-road-labels[zoom>=17][highway=motorway] name
{
    text-fill: #fdf6e3;
    text-halo-fill: #d33682;
    text-face-name: 'DejaVu Sans Condensed Bold';
}

#major-road-labels[zoom>=17][highway=trunk] name,
#major-road-labels[zoom>=17][highway=primary] name,
#major-road-labels[zoom>=17][highway=secondary] name,
#minor-road-labels[zoom>=17][highway=tertiary] name
{
    text-fill: #fdf6e3;
    text-halo-fill: #657b83;
    text-face-name: 'DejaVu Sans Condensed Bold';
}

#minor-road-labels[zoom>=18] name
{
    text-fill: #fdf6e3;
    text-halo-fill: #93a1a1;
    text-face-name: 'DejaVu Sans Condensed Bold';
}
