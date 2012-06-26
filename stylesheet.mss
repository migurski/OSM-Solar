/*ocean*/
Map { 
	map-bgcolor: #073642; } 

/*lakes*/
#water-bodies-low[zoom<11],
#water-bodies-med[zoom>=11][zoom<14],
#water-bodies-high[zoom>=14]
{ 
	polygon-fill: #073642;
}

/*land, map background*/
#land { 
	polygon-fill: #fdf6e3; }

#buildings-med[area>=16000][zoom=12],
#buildings-med[area>=8000][zoom=13],
#buildings-high[area>=4000][zoom=14],
#buildings-high[area>=2000][zoom=15],
#buildings-high[area>=1000][zoom=16],
#buildings-high[zoom>=17]
{
    polygon-fill: #eee8d5;
}

/*//////// Base line styles */

.roads {
	line-join: round;
	line-cap: round;
}

.roads[render=outline],
.roads[render=casing]
{
    line-cap: butt;
}


/*//////// Colors */

.roads[kind=highway][render=inline]
{
	line-color: #d33682;
}

.roads[kind=major_road][render=inline]
{
	line-color: #657b83;
}

.roads[kind=minor_road][render=inline]
{
	line-color: #93a1a1;
}

.roads[kind=rail][render=inline],
.roads[kind=rail][render=casing],
.roads[kind=rail][render=outline]
{
	line-color: #93a1a1;
}

.roads[kind=path][render=inline]
{
	line-color: #93a1a1;
	line-dasharray: 2,5;
}

/*//////// Zoom Level 10 */

#z10-roads[zoom=10][kind=highway][render=inline]
{ 	
	line-width: 2;
}

#z10-roads[zoom=10][kind=major_road][render=inline]
{ 	
	line-width: 2; 
}

#z10-roads[zoom=10][kind=minor_road][render=inline]
{ 	
	line-width: 1; 
}

/*//////// Zoom Level 11 */

#z11-roads[zoom=11][kind=highway][render=inline]
{ 	
	line-width: 3;
}

#z11-roads[zoom=11][kind=major_road][render=inline]
{ 	
	line-width: 2; 
}

#z11-roads[zoom=11][kind=minor_road][render=inline]
{ 	
	line-width: 1; 
}

/*//////// Zoom Level 12 */

#z12-roads[zoom=12][kind=highway][is_link=no][render=inline]
{ 	
	line-width: 3;
}

#z12-roads[zoom=12][kind=major_road][render=inline]
{ 	
	line-width: 2; 
}

#z12-roads[zoom=12][kind=minor_road][render=inline]
{ 	
	line-width: 1;
}

/*//////// Zoom Level 13 */

#z13-roads[zoom=13][kind=highway][is_link=no][render=inline]
{ 
	line-width: 4;
}

#z13-roads[zoom=13][kind=highway][is_link=yes][render=inline]
{ 
	line-width: 1;	
}

#z13-roads[zoom=13][kind=major_road][render=inline]
{ 	
	line-width: 3;
}

#z13-roads[zoom=13][kind=minor_road][render=inline]
{
 	line-width: 1.5;
}

/*//////// Zoom Level 14 */

#z14-roads[zoom=14][kind=highway][render=inline]
{
	line-width: 4;
}

#z14-roads[zoom=14][kind=highway][is_link=yes][render=inline]
{
	line-width: 2.5;	
}

#z14-roads[zoom=14][kind=major_road][render=inline]
{
	line-width: 4;
}

#z14-roads[zoom=14][kind=major_road][is_link=yes][render=inline]
{
	line-width: 2;
}

#z14-roads[zoom=14][kind=minor_road][render=inline]
{
	line-width: 2.5;
}

#z14-roads[zoom=14][kind=rail][render=inline]
{
	line-width: 1;
}

#z14-roads[zoom=14][kind=rail][render=casing]
{
	line-width: 3;
	line-dasharray: 1,3;
	line-cap: butt;
}

/*//////// Zoom Level 15 */

#z15plus-roads[zoom=15][kind=highway][render=inline]
{
	line-width: 7;
}

#z15plus-roads[zoom=15][kind=highway][is_link=yes][render=inline]
{
	line-width: 3;	
}

#z15plus-roads[zoom=15][kind=major_road][render=inline]
{
	line-width: 5;
}

#z15plus-roads[zoom=15][kind=major_road][is_link=yes][render=inline]
{
	line-width: 2.5;
}

#z15plus-roads[zoom=15][kind=minor_road][render=inline]
{
	line-width: 4;
}

#z15plus-roads[zoom=15][highway=service][render=inline]
{
	line-width: 2.5;
}

#z15plus-roads[zoom=15][kind=rail][render=inline]
{
	line-width: 1;
}

#z15plus-roads[zoom=15][kind=rail][render=casing]
{
	line-width: 3;
	line-dasharray: 1,3;
	line-cap: butt;
}

#z15plus-roads[zoom=15][kind=path][render=inline]
{
	line-width: 1; 
	line-dasharray: 2,3;
	line-cap: butt;
}

/*//////// Zoom Level 16 */

#z15plus-roads[zoom=16][kind=highway][render=inline]
{
	line-width: 9;
}

#z15plus-roads[zoom=16][kind=highway][is_link=yes][render=inline]
{
	line-width: 4;
}

#z15plus-roads[zoom=16][kind=major_road][render=inline]
{
	line-width: 7;
}

#z15plus-roads[zoom=16][kind=major_road][is_link=yes][render=inline]
{
	line-width: 4;
}

#z15plus-roads[zoom=16][kind=minor_road][render=inline]
{
	line-width: 4;
}

#z15plus-roads[zoom=16][highway=service][render=inline]
{
	line-width: 2.5;
}

#z15plus-roads[zoom=16][kind=rail][render=inline]
{
	line-width: 1;
}

#z15plus-roads[zoom=16][kind=rail][render=casing]
{
	line-width: 5;
	line-dasharray: 1,4;
	line-cap: butt;
}

#z15plus-roads[zoom=16][kind=path][render=inline]
{
	line-width: 1;
	line-dasharray: 2,3;
	line-cap: butt;
}

/*//////// Zoom Level 17 */

#z15plus-roads[zoom=17][kind=highway][render=inline]
{
	line-width: 16;
}

#z15plus-roads[zoom=17][kind=highway][is_link=yes][render=inline]
{
	line-width: 7;
}

#z15plus-roads[zoom=17][kind=major_road][render=inline]
{
	line-width: 14;
}

#z15plus-roads[zoom=17][kind=major_road][is_link=yes][render=inline]
{
	line-width: 7;
}

#z15plus-roads[zoom=17][kind=minor_road][render=inline]
{
	line-width: 8;
}

#z15plus-roads[zoom=17][highway=service][render=inline]
{
	line-width: 5;
}

#z15plus-roads[zoom=17][kind=rail][render=inline]
{
	line-width: 1;
}

#z15plus-roads[zoom=17][kind=rail][render=casing]
{
	line-width: 5;
	line-dasharray: 1,4;
	line-cap: butt;
}

#z15plus-roads[zoom=17][kind=path][render=inline]
{
	line-width: 2; 
	line-dasharray: 4,6;
	line-cap: butt;
}
	
	
/*//////// Zoom Level 18+ */

#z15plus-roads[zoom>=18][kind=highway][render=inline]
{
	line-width: 28;
}

#z15plus-roads[zoom>=18][kind=highway][is_link=yes][render=inline]
{
	line-width: 10;
}

#z15plus-roads[zoom>=18][kind=major_road][render=inline]
{
	line-width: 17;
}

#z15plus-roads[zoom>=18][kind=major_road][is_link=yes][render=inline]
{
	line-width: 10;
}

#z15plus-roads[zoom>=18][kind=minor_road][render=inline]
{
	line-width: 11;
}

#z15plus-roads[zoom=18][kind=rail][render=inline]
{
	line-width: 2;
}

#z15plus-roads[zoom=18][kind=rail][render=casing]
{
	line-width: 7;
	line-dasharray: 2,6;
	line-cap: butt;
}

#z15plus-roads[zoom>=18][kind=path][render=inline]
{
	line-width: 2; 
	line-dasharray: 4,6;
	line-cap: butt;
}
