import random
from nodes import NODE_CLASS_MAPPINGS

class IsulionPromptGenerator:
    styles = [
		'3D Rendering','Abstract Art','Aerial Photography','Airbrush Art','Anime','Architectural Photography','Art Brut','Art Deco','Art Nouveau','Assemblage','Avant-garde','Baroque','Black and White Photography','Calligraphy','Caricature','Charcoal Drawing','Chiaroscuro','Cinematic Photography','Classicism','Collage','Comic Book Style','Concept Art','Constructivism','Cubism','Cyberpunk','Dadaism','Digital Art','Dotwork','Drawing','Eco-Art','Egyptian Art','Engraving','Etching','Expressionism','Fantasy Art','Fashion Photography','Fauvism','Film Still','Fine Art Photography','Flat Design','Food Photography','Found Art','Fresco','Futurism','Geometric Art','Glitch Art','Gothic Art','Graffiti','Graffiti Art','HDR Photography','Hyperrealism','Iconography','Illustration','Impressionism','Ink Drawing','Infrared Photography','Installation Art','Isometric Art','Japanese Ink Art','Kinetic Art','Landscape Photography','Lithography','Long Exposure','Low Poly','Macro Photography','Manga Style','Matte Painting','Minimalism','Minimalist','Mixed Media','Muralism','Neo-Classicism','Night Photography','Oil Painting','Op Art','Panoramic Photography','Pastel Art','Pencil Sketch','Performance Art','Photojournalism','Photorealism','Pixel Art','Pointillism','Pop Art','Portrait Photography','Post-Impressionism','Postmodern Art','Printmaking','Realism','Retro','Rococo','Romanticism','Sculpture','Sci-Fi Art','Sepia','Steampunk','Still Life','Street Art','Street Photography','Surrealism','Synthwave','Tilt-Shift Photography','Typography Art','Ukiyo-e','Underwater Photography','Urban Art','Vector Art','Vibrant Colors','Vintage','Watercolor','Wildlife Photography','Woodcut'
    ]

    color_palettes = [
		'Analogous Colors','Autumn Leaves','Black and White','Bright Neons','Bright Warm Tones','Complementary Colors','Cool Colors','Cyberpunk Palette','Desert Sand Palette','Duotone','Earth Tones','Earthy Greens','Electric Blue','Fiery Reds','Fluorescent Colors','Forest Greens','Golden Tones','Grayscale','High Contrast','Jewel Tones','Low Contrast','Metallic Hues','Minimalist Palette','Monochrome','Monotone Palette','Muted Colors','Neon Colors','Neon Noir','Oceanic Palette','Pastel Colors','Pastel Rainbow','Pop Art Palette','Primary Colors','Rainbow','Retro Colors','Rose Gold','Royal Blues','Secondary Colors','Sepia','Shadow Palette','Smoky Shades','Soft Pinks','Spring Blossoms','Steampunk Palette','Summer Vibes','Sunset Palette','Triadic Colors','Tropical Palette','Twilight Palette','Vibrant Colors','Vintage Colors','Warm Colors','Winter Frost'
    ]
    subjects = [
        'A beautiful landscape with rolling hills','A calm lake reflecting the mountains','A blooming cherry blossom tree','A deserted beach with golden sand','A close-up of a butterfly on a flower','A dramatic sunset over the ocean','A starry night sky with a full moon','A waterfall in a tropical rainforest','A snow-covered forest in winter','A desert landscape with sand dunes','An old lighthouse by the sea','A field of sunflowers under a blue sky','A tranquil Japanese garden','A vintage car parked on a cobblestone street','A herd of wild horses running free','A misty mountain range at dawn','A colorful hot air balloon in the sky','A rustic barn in the countryside','A rainbow over a meadow','A coral reef teeming with fish','An abandoned castle on a hill','A glacier floating in the Arctic sea','A forest path covered in autumn leaves','A meteor shower in the night sky','A crystal-clear lake surrounded by trees','A canyon with layered rock formations','A farm with fields of wheat','A tropical island with palm trees','A futuristic city with skyscrapers','A galaxy with swirling stars','A steampunk airship sailing the skies','A dragon flying over mountains','An enchanted forest with glowing plants','A robot exploring a distant planet','An ancient ruin overgrown with vines','A lighthouse during a stormy night','A snow-capped volcano','A whimsical treehouse in a forest','A crystal cave illuminated by light','A serene meadow filled with wildflowers','A giant mushroom in a fantasy world','A futuristic spacecraft orbiting Earth','A bridge shrouded in fog','A close-up of a snowflake','An iceberg drifting in the sea','A tropical rainforest canopy','A serene Zen garden','A colorful coral reef underwater','A volcano erupting with lava','An aurora borealis over snowy mountains','A sunflower field at sunset','A majestic eagle soaring in the sky','A mysterious cave entrance','A close-up of a dewdrop on a leaf','An old windmill on a hill','A sailboat on a calm lake','A stone bridge over a river','A cloudscape with dramatic lighting','A field of lavender in bloom','A rustic cabin in the woods','A vibrant carnival mask','A wolf howling at the moon','A futuristic robot','An underwater shipwreck','A galaxy with colorful nebulas','A tranquil pond with koi fish','A hot air balloon festival','An ancient tree with sprawling roots','A city skyline at night','A peacock displaying its feathers','A herd of elephants in the savannah','A rustic lighthouse at sunset','A mountain reflected in a lake','A whimsical fairy tale castle','A desert cactus in bloom','A glowing jellyfish underwater','A farmyard with animals','A field of poppies','An iceberg under the northern lights','A thunderstorm over the ocean','A Japanese pagoda surrounded by trees','A starfish on the sandy beach','A futuristic city floating in the sky','A rainbow over a waterfall','A whale breaching the water','A snowy owl in flight','A medieval castle with towers','A dragonfly resting on a leaf','A moss-covered forest floor','A coral reef with sea turtles','An old steam locomotive','A flock of birds migrating','A solar eclipse','A meadow with grazing deer','A space station orbiting Earth','A close-up of a ladybug','A wind farm with turbines','A colorful cityscape at dusk','A field of pumpkins in autumn','A sea turtle swimming','A comet streaking across the sky','A river flowing through a canyon','A giant sequoia tree','A blooming cactus flower','A polar bear on ice','A vibrant coral garden','A mystical foggy forest','A vineyard with ripe grapes','A futuristic monorail train','A sunset over the desert','A pack of wolves in the snow','A colorful parrot in the jungle','A floating lantern festival','A koi pond with lily pads','A spiral galaxy','A stormy sea with high waves','An old ship sailing at sea','A butterfly garden','A field of golden wheat','A mountain peak above the clouds','A robot in a futuristic lab','A close-up of a honeybee on a flower','A rustic stone cottage','A tropical fish in a coral reef','A desert landscape with rock arches','A snowy mountain lodge','A golden retriever playing','A windmill in a tulip field','A forest stream with rocks','A thunderstorm over a city','A field of daisies','A seagull flying over the ocean','A galaxy cluster in space','A red fox in the forest','An ancient temple in the jungle','A frozen waterfall in winter','A futuristic car speeding','A close-up of a peacock feather','A pumpkin patch at harvest','A snowy village during Christmas','A bioluminescent beach at night','A rustic bridge in the forest','A comet passing near Earth','A sunflower facing the sun','An underwater cave with stalactites','A rainbow-colored hot air balloon','A desert landscape with mesas','A castle on a cliff by the sea','A close-up of a hummingbird','A field of bluebells','An old clock tower','A dolphin jumping out of the water','A futuristic city underwater','A glowing mushroom in a dark forest','A windmill under the stars','A crystal-clear mountain stream','A galaxy with spiral arms','A hot spring in a snowy landscape','A snowy owl perched on a branch','A canyon with a river at the bottom','A steam locomotive crossing a bridge','A futuristic spacecraft landing','A rose garden in full bloom','A lightning bolt in the night sky','A penguin colony on ice','A waterfall cascading into a pool','A desert with cacti at sunset','A meadow with grazing sheep','An old library filled with books','A close-up of a seashell','A robot in a meadow','A tranquil pond with lotus flowers','A mountain range during sunrise','A starry sky over the desert','A lighthouse illuminating the night','A forest blanketed in fog','A colorful sunset over the ocean','A butterfly emerging from a cocoon','An ancient oak tree','A space nebula with vibrant colors','A desert road stretching into the horizon','A hot air balloon over vineyards','A galaxy with twin stars','A whale shark swimming','A field of lavender at dusk','A glacier melting into the sea','A comet tail in deep space','A rainbow over rolling hills','A futuristic city with flying cars','A wolf pack in the wilderness','A dragon curled around a tower','A coral reef with clownfish','An old windmill by a lake','A mountain reflected in still water','A fantasy castle in the clouds','A stormy sky with dark clouds','A close-up of a leaf with raindrops','A desert landscape with mirages','An aurora over a frozen lake','A steampunk clock with gears','A cherry blossom festival','A peacock spreading its feathers','A rustic farmhouse with fields','A sea turtle swimming underwater','A meadow with wildflowers','A hummingbird hovering near a flower','A futuristic robot exploring','A field of red poppies','A dragonfly over a pond','A crystal chandelier sparkling','A snowy landscape with pine trees','A rainbow over a city skyline','A sunset over the plains','A close-up of an eye with reflection','A snowy mountain reflected in a lake','A galaxy with a black hole','A stormy sea with lightning','A hot air balloon over a desert','A waterfall surrounded by greenery','A field of sunflowers facing the sun','An ancient bridge over a river','A robot hand holding a flower','A forest with tall redwood trees','A close-up of a cat s eye','A dragon flying over a city','A desert with towering sand dunes','A starfish on the ocean floor','A comet passing by a planet','A field of tulips in spring','A wolf standing on a rock','An underwater scene with dolphins','A vintage bicycle against a wall','A snowy path through the woods','A galaxy with colorful gases','A mountain range during sunset','A bridge lit up at night','A close-up of a snail on a leaf','A field of daisies under a blue sky','A coral reef with exotic fish','A hot air balloon over mountains','A futuristic spaceship in space','A rainbow over a waterfall','A forest with sunbeams through trees','A lion resting in the grass','A castle surrounded by a moat','A crystal ball on a stand','A forest floor with mushrooms','A sunset over the ocean waves','A snowy owl in flight','A robot in a cityscape','A meadow with butterflies','A mountain reflected in a lake','A colorful nebula in space','A thunderstorm over fields','A coral reef with sea horses','A desert with a single cactus','An old shipwreck on the beach','A galaxy with shooting stars','A windmill under a cloudy sky','A tiger walking through the jungle','A futuristic city with neon lights','A hot air balloon over fields','A waterfall in a tropical setting','A field of lavender in bloom','A close-up of a dragonfly wing','A robot with glowing eyes','A snowy landscape at dawn','A galaxy with swirling colors','A lighthouse during sunset','A peacock feather in detail','A meadow with grazing horses','A coral reef with manta rays','A mountain covered in fog','A desert with a mirage','A close-up of a crystal','A rainbow over green hills','A futuristic skyline','A wolf howling in the moonlight','A hot air balloon over the ocean','A galaxy with planets aligning','A forest with autumn colors','A robot standing in a field','A snowy mountain under stars','A waterfall in a forest','A meadow with wildflowers','A desert landscape at dusk','A coral reef with colorful fish','A close-up of a sunflower','A lighthouse on a cliff','A futuristic vehicle in motion','A wolf pack in the snow','A field of wheat waving in the wind','A galaxy with bright stars','A robot hand reaching out','A mountain range at sunrise','A rainbow over the ocean','A forest with fog','A butterfly on a leaf','A hot air balloon at sunrise','A coral reef with jellyfish','A desert with rock formations','A field of sunflowers','A robot in a futuristic city','A snowy landscape with aurora','A waterfall in a canyon','A close-up of a leaf vein','A galaxy with cosmic dust','A lighthouse in a storm','A meadow with grazing cows','A mountain reflected in water','A rainbow over mountains','A robot exploring ruins','A forest with sun rays','A hot air balloon over a lake','A coral reef with starfish','A desert landscape with cacti','A field of lavender at sunset','A wolf in the forest','A futuristic city with flying vehicles','A galaxy with multiple planets','A close-up of a water droplet','A snowy mountain peak','A waterfall in the mountains','A meadow with daisies','A robot looking at the stars','A rainbow over a forest','A butterfly garden in bloom','A desert with a lone tree','A coral reef with coral formations','A mountain landscape in autumn','A hot air balloon over fields','A forest with colorful leaves','A robot in a lab','A galaxy with spiral arms','A wolf standing on a cliff','A lighthouse by the sea','A field of tulips in spring','A waterfall with a rainbow','A meadow under a blue sky','A coral reef with bright colors','A mountain at dusk','A desert sunset','A robot with a glowing core','A butterfly resting on a flower','A galaxy with nebulae','A snowy landscape with trees','A hot air balloon festival','A forest with a clear stream','A wolf howling at the moon','A meadow filled with poppies','A robot in a desert','A rainbow over a city','A mountain range with snow','A coral reef with fish','A waterfall surrounded by rocks','A field of sunflowers','A galaxy with distant stars','A desert with dunes','A close-up of an insect wing','A robot in an industrial area','A snowy mountain under a full moon','A meadow with a small pond','A butterfly on a blade of grass','A hot air balloon over mountains','A forest with dense trees','A wolf running through snow','A rainbow over a meadow','A coral reef with sea life','A mountain with a glacier','A robot standing on a hill','A galaxy with colorful gases','A waterfall in a tropical forest','A desert landscape at night','A meadow with wildflowers','A butterfly landing on a plant','A lighthouse guiding ships','A close-up of raindrops on petals','A robot reaching for the sky','A hot air balloon over vineyards','A snowy landscape with cabins','A galaxy with bright stars','A forest with mist','A wolf in a meadow','A coral reef with diverse life','A mountain during golden hour','A desert with a caravan of camels','A waterfall in a hidden valley','A rainbow over rolling hills','A robot exploring an alien world','A butterfly garden in spring','A meadow with tall grasses','A galaxy with twin suns','A hot air balloon above clouds','A wolf under the northern lights','A coral reef with sharks','A mountain with a clear sky','A desert landscape with rocks','A waterfall into a clear pool','A rainbow over a lighthouse'
    ]
    
    lightings = [
		'Accent Lighting','Ambient Lighting','Artificial Lighting','Backlighting','Bicolor Lighting','Bottom Lighting','Bounce Lighting','Candlelight','Chiaroscuro','Chromatic Lighting','Colored Lighting','Cross Lighting','Diffuse Lighting','Directional Lighting','Direct Lighting','Dramatic Lighting','Edge Lighting','Fill Lighting','Firelight','Flat Lighting','Fluorescent Lighting','Frontal Lighting','Frosted Lighting','Gaffer Lighting','Glamour Lighting','Golden Hour','Halo Lighting','Hard Light','High Key','Incandescent Lighting','Industrial Lighting','Interior Lighting','Kicker Lighting','LED Lighting','Low Key','Magic Hour','Moonlight','Morning Light','Motivated Lighting','Natural Light','Neon Lighting','Night Lighting','Outdoor Lighting','Overhead Lighting','Overcast','Practical Lighting','Profile Lighting','Prop Lighting','Puddle Lighting','Radiant Lighting','Reflective Lighting','Rembrandt Lighting','Rim Lighting','Ring Light','Sidelight','Side Lighting','Silhouette Lighting','Soft Light','Specular Lighting','Spotlight','Starlight','Strip Lighting','Studio Lighting','Strobe Lighting','Subsurface Scattering','Sunbeam Lighting','Sunlight','Sunrise','Sunset','Surface Lighting','Top Lighting','Track Lighting','Tungsten Lighting','Twilight Lighting','Underexposed Lighting','Underwater Lighting','UV Lighting','Warm Lighting','Water Reflected Lighting','Window Lighting','Winter Lighting','Xenon Lighting','Candle Glow','Crossover Lighting','Diffraction Lighting','Electric Glow','Filament Lighting','Flickering Light','Fluorescence Light','Ghost Lighting','Incandescent Glow','LED Glow','Lightning Bolt','Moon Glow','Neon Glow','Night Glow','Overhead Glow','Pinhole Light','Rim Glow','Side Glow','Twilight Glow','Sunset Glow'
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "randomize": (["enable", "disable"],),
                "seed": ("INT", {"default": 0, "min": 0, "max": 999999999}),
                "style": (cls.styles,),
                "subject": (cls.subjects,),
                "color_palette": (cls.color_palettes,),
                "lighting": (cls.lightings,)
            }
        }

    RETURN_TYPES = ("STRING", "INT",)  # Two outputs: prompt string and seed
    FUNCTION = "choose_style_palette_and_lighting"
    CATEGORY = "Art/Styles"

    def choose_style_palette_and_lighting(self, randomize, seed, style, color_palette, lighting, subject):
        if randomize == "enable":
            # If seed is provided and greater than zero, set it for the random generator
            if seed is not None and seed > 0:
                random.seed(seed)
            else:
                seed = random.randint(0, 999999999)  # Generate a random seed if none is provided
                random.seed(seed)

            style = random.choice(self.styles)
            color_palette = random.choice(self.color_palettes)
            lighting = random.choice(self.lightings)
            subject = random.choice(self.subjects)

        # Return the prompt and the seed as two separate outputs
        return (f"Subject: {subject}\nStyle: {style}\nColor Palette: {color_palette}\nLighting: {lighting}", seed)

# Register the node with ComfyUI
NODE_CLASS_MAPPINGS.update({
    "IsulionPromptGenerator": IsulionPromptGenerator
})