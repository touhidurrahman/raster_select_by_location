layerlist = [layer for layer in QgsProject.instance().mapLayers().values()] # List all layers added to the map

selected_features = iface.activeLayer().selectedFeatures() # Get selected features from the active layer

if len(selected_features) > 0: # Check if features are selected
    selected_feature = selected_features[0] # Consider the first selected feature
    selected_feature_extent = selected_feature.geometry().boundingBox() # Get the extent of the selected feature

    for layer in layerlist:
        if layer.extent().intersects(selected_feature_extent): # If layer extent intersects selected feature's extent
            print(layer.name())
else:
    print("No features selected.")
