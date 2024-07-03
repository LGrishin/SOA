<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Городской навигатор</title>
    <!-- <link rel="stylesheet" href="styles.css"> -->
</head>
<body>
    <div class="map">
        <!-- <img class="icon" src="map.svg" alt="dots icon"> -->
        <svg id="svg2"  width="700" height="700" viewBox="0 0 500 670" xmlns="http://www.w3.org/2000/svg" xmlns:bx="https://boxy-svg.com">
            <desc>Source: openclipart.org/detail/209545</desc>
            <defs/>
            <rect id="polys" x="95.787" y="153.158" width="123.96" height="60.443" style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);"/>
            <rect id="polys" x="283.265" y="495.877" width="79.908" height="191.793" style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0); transform-box: fill-box; transform-origin: 50% 50%;" transform="matrix(0.48481, 0.87462, -0.87462, 0.48481, -4.45215, -215.583384)"/>
            <rect id="polys" x="307.852" y="140.864" width="124.985" height="79.908" style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);"/>
            <rect id="polys" x="118.326" y="266.873" width="108.593" height="38.93" style="stroke: rgb(0, 0, 0); fill: rgb(211, 211, 211);"/>
            <rect id="polys" x="98.861" y="461.521" width="110.642" height="31.758" style="stroke: rgb(0, 0, 0); transform-box: fill-box; transform-origin: 50% 50%; fill: rgb(209, 209, 209);" transform="matrix(0.669131, 0.743145, -0.743145, 0.669131, 23.98794, 3.689997)"/>
            <rect id="polys" x="351.904" y="502.5" width="77.859" height="26.636" style="stroke: rgb(0, 0, 0); fill: rgb(212, 55, 55);"/>
            <rect id="polys" x="54.809" y="338.586" width="112.691" height="23.563" style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);"/>
            <rect id="polys" x="47.638" y="524.014" width="80.519" height="22.538" style="stroke: rgb(0, 0, 0); fill: rgb(57, 57, 219);"/>
            <rect id="polys" x="157.255" y="82.469" width="97.324" height="21.514" style="stroke: rgb(0, 0, 0); fill: rgb(213, 64, 64);"/>
            <rect id="polys" x="361.124" y="42.003" width="86.055" height="22.538" style="stroke: rgb(0, 0, 0); fill: rgb(57, 57, 219);"/>
            <path id="skel" style="stroke: rgb(0, 0, 0); fill: none;" d="M 311.95 299.656 L 416.445 279.167 L 448.203 365.222 L 440.008 446.154 L 358.05 469.717 L 301.705 472.79 L 303.754 577.286 L 479.962 579.335 L 480.986 479.962"/>
            <path id="skel" style="stroke: rgb(0, 0, 0); fill: none;" d="M 298.632 116.277 L 256.628 147.011 L 262.775 229.992 L 315.023 299.656 L 243.31 326.292 L 106.032 318.096 L 46.613 232.041 L 71.2 83.494 L 132.668 33.295 L 265.849 38.417 L 304.778 111.154 L 458.448 126.521 L 461.521 242.286 L 417.469 277.118"/>
            <path id="skel" style="stroke: rgb(0, 0, 0); fill: none;" d="M 304.779 114.228 L 65.054 127.546 L 94.763 156.231"/>
            <path id="skel" style="stroke: rgb(0, 0, 0); fill: none;" d="M 46.613 225.894 L 265.849 234.09"/>
            <path id="skel" style="stroke: rgb(0, 0, 0); fill: none;" d="M 198.234 118.326 L 198.234 101.934"/>
            <path id="skel" style="stroke: rgb(0, 0, 0); fill: none;" d="M 393.907 504.549 L 361.124 470.742"/>
            <path id="skel" style="stroke: rgb(0, 0, 0); fill: none;" d="M 478.937 480.986 L 440.008 442.057"/>
            <path id="skel" style="stroke: rgb(0, 0, 0); fill: none;" d="M 302.729 475.864 L 240.237 491.231 L 165.451 391.858 L 234.09 326.292"/>
            <path id="skel" style="stroke: rgb(0, 0, 0); fill: none;" d="M 302.729 578.31 L 28.173 599.824 L 26.124 446.154 L 167.5 389.809 L 31.246 381.613 L 47.638 232.041"/>
            <path id="skel" style="stroke: rgb(0, 0, 0); fill: none;" d="M 309.901 110.13 L 361.124 68.127 L 268.922 38.417"/>
            <path id="skel" style="stroke: rgb(0, 0, 0); fill: none;" d="M 456.399 125.497 L 480.986 19.977 L 269.947 36.369"/>
            <path id="skel" style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);" d="M 404.151 63.005 L 405.176 121.399"/>
            <path id="skel" style="fill: none; stroke: rgb(0, 0, 0);" d="M 89.641 520.94 L 82.469 425.665"/>
            <path id="gr" style="stroke-width: 7px; fill: none; stroke: rgb(242, 0, 0);" d="M 86.567 524.014 L 86.055 507.11 C 85.543 490.207 84.518 456.399 98.007 434.203 C 111.496 412.006 139.498 401.419 168.354 382.979 C 197.209 364.539 226.919 338.244 243.481 303.925 C 260.043 269.605 263.458 227.261 256.97 197.551 C 250.482 167.842 234.09 150.767 226.407 136.766 C 218.723 122.765 219.748 111.838 220.26 106.374 L 220.772 100.91" bx:d="M 86.567 524.014 U 83.494 422.592 U 167.5 390.833 U 256.628 311.95 U 266.873 184.916 U 217.699 133.693 U 220.772 100.91 1@5adf4346"/>
            <path id="gr" style="stroke-width: 7px; fill: none; stroke: rgb(85, 88, 218);" d="M 390.833 503.524 L 390.662 494.133 C 390.492 484.742 390.15 465.961 399.883 443.935 C 409.615 421.909 429.422 396.639 434.373 368.808 C 439.325 340.976 429.421 310.584 405.005 294.021 C 380.588 277.459 341.659 274.727 315.364 258.848 C 289.07 242.969 275.41 213.942 274.898 187.477 C 274.386 161.012 287.021 137.107 309.73 126.009 C 332.439 114.911 365.222 116.618 383.15 110.13 C 401.078 103.642 404.152 88.958 405.688 81.616 L 407.225 74.274" bx:d="M 390.833 503.524 U 389.809 447.179 U 449.228 371.369 U 419.518 280.191 U 302.729 271.995 U 261.751 184.916 U 299.656 113.203 U 398.005 118.326 U 407.225 74.274 1@c6b9d8c7"/>
            <polyline id="det" style="fill: none; stroke: rgb(41, 0, 236);" points="392.383 499.231 391.461 441.107 425.597 397.745 435.746 376.525 435.746 348.846 422.829 297.18 383.157 285.187 309.349 261.199 279.825 217.836 278.903 140.337 306.581 125.576 394.229 120.04 412.681 93.285 411.758 62.838"/>
            <polyline id="det" style="fill: none; stroke: rgb(244, 0, 0);" points="88.846 523.219 83.31 422.655 255.838 329.472 255.838 187.39 220.779 143.105 221.701 101.588"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(107, 211, 85, 0.5);" points="255.604 456.399 353.953 504.549 430.787 500.451 422.592 364.197"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(107, 211, 85, 0.5);" points="430.787 498.402 422.592 365.222 498.402 269.946 499.427 657.194"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(107, 211, 85, 0.5);" points="422.592 361.124 381.613 293.509 379.564 220.772 499.427 221.797 499.427 271.995"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(107, 211, 85, 0.5);" points="430.787 141.888 449.228 64.029 299.656 66.078 309.901 141.888"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(107, 211, 85, 0.5);" points="307.504 219.682 221.701 213.223 220.779 104.356 305.658 111.737"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(107, 211, 85, 0.5);" points="220.779 215.991 226.314 266.734 313.04 334.084 379.467 295.335 378.544 220.605"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(107, 211, 85, 0.5);" points="228.159 271.348 228.159 377.447 310.271 335.007"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(107, 211, 85, 0.5);" points="225.392 305.484 166.345 307.329 167.267 407.893 225.392 376.525"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(107, 211, 85, 0.5);" points="165.422 363.608 166.345 423.578 78.697 428.191 76.852 361.763"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(107, 211, 85, 0.5);" points="128.518 425.423 128.518 524.142 49.174 524.142 48.251 433.726"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="60.245 149.563 219.856 153.254 218.933 102.511 64.858 101.588"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="220.779 208.61 224.469 265.812 39.948 269.502 43.638 211.378"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="158.041 428.191 230.005 511.225 261.373 467.863 209.707 388.518"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="45.483 270.425 39.948 301.793 116.524 305.484 118.369 268.58"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="129.441 549.975 47.329 549.975 47.329 615.48 124.828 614.557"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="63.936 152.331 46.406 212.301 94.382 208.61 92.536 155.099"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="433.861 219.748 431.812 142.913 500.451 1.537 500.451 222.821"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="256.76 41.619 257.683 102.511 304.736 109.891 292.742 37.006"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="255.838 83.136 73.162 84.981 130.363 21.321 255.838 27.779"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="264.141 463.25 153.428 619.17 340.717 621.015 349.944 503.844"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="130.342 454.024 128.518 618.248 150.406 618.248 207.862 537.96"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="350.866 530.6 341.64 617.325 480.954 614.557 441.281 525.987"/>
            <polygon id="tes" style="stroke: rgb(0, 0, 0); fill: rgba(252, 0, 0, 0.455);" points="165.422 306.407 41.793 300.871 37.18 341.466 166.345 341.466"/>

        </svg>    </div>
        <style> 
            #skel {
                stroke-dasharray: 1000;
                stroke-dashoffset: 1000;
                animation: draw 4s linear forwards, hide 2s forwards 10s;
            }   /*16*/
            
            #gr {
                stroke-dasharray: 1000;
                stroke-dashoffset: 1000;
                animation: draw 5s linear forwards 4s, hide 2s forwards 14s;
            }   /*29*/
            
            #det {
                stroke-dasharray: 1000;
                stroke-dashoffset: 1000;
                animation: draw 7s linear forwards;
                animation-delay: 16s;
            }
            
            #tes {
                stroke-dasharray: 1000;
                stroke-dashoffset: 1000;
                fill-opacity: 0;
                animation: draw 4s linear forwards 10s, hide 2s forwards 22s;
            }
            
            @keyframes draw {
                0% {
                  stroke-dashoffset: 1000;
                  fill-opacity: 0;
                }
                100% {
                  stroke-dashoffset: 0;
                  fill-opacity: 1;
                }
            }
            
            @keyframes hide {
                0% {
                  opacity: 1;
                }
                100% {
                  opacity: 0;
                  fill-opacity: 0;
                }
            }
        </style>
    <script src="script.js"></script>
</body>
</html>
