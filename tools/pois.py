def get_mock_pois(location):
    pois = {
        # Mexico
        "Puebla": ["Puebla Cathedral", "Callejón de los Sapos", "Amparo Museum"],
        "Tehuacán": ["Tehuacán-Cuicatlán Biosphere Reserve", "Water Museum"],
        "Oaxaca": ["Santo Domingo Temple", "Monte Albán", "20 de Noviembre Market"],
        
        # Germany
        "Frankfurt": ["Römerberg Square", "Städel Museum", "Main Tower Viewpoint"],
        
        # France
        "Strasbourg": ["Petite France", "Strasbourg Cathedral", "European Parliament"],
        "Lyon": ["Basilica of Notre-Dame de Fourvière", "Old Lyon", "Traboules"],
        
        # Spain
        "Barcelona": ["Sagrada Familia", "Park Güell", "Gothic Quarter"],
        "Madrid": ["Prado Museum", "Royal Palace", "Retiro Park"],

        # Italy
        "Rome": ["Colosseum", "Trevi Fountain", "Vatican Museums"],
        "Florence": ["Uffizi Gallery", "Duomo", "Ponte Vecchio"],
    }

    return pois.get(location, ["Generic tourist site"])