

CREATE TABLE "ImageDataset" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT NOT NULL, 
	x_direction VARCHAR(21), 
	y_direction VARCHAR(21), 
	z_direction VARCHAR(21), 
	x_size INTEGER, 
	y_size INTEGER, 
	z_size INTEGER, 
	x_resolution FLOAT, 
	y_resolution FLOAT, 
	z_resolution FLOAT, 
	unit VARCHAR(2), 
	revision_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(revision_of) REFERENCES "ImageDataset" (id)
);

CREATE TABLE "ParcellationTerminology" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT NOT NULL, 
	revision_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(revision_of) REFERENCES "ParcellationTerminology" (id)
);

CREATE TABLE "AnatomicalSpace" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT NOT NULL, 
	measures TEXT NOT NULL, 
	revision_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(measures) REFERENCES "ImageDataset" (id), 
	FOREIGN KEY(revision_of) REFERENCES "AnatomicalSpace" (id)
);

CREATE TABLE "ParcellationColorScheme" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT NOT NULL, 
	subject_parcellation_terminology TEXT NOT NULL, 
	revision_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject_parcellation_terminology) REFERENCES "ParcellationTerminology" (id), 
	FOREIGN KEY(revision_of) REFERENCES "ParcellationTerminology" (id)
);

CREATE TABLE "ParcellationTermSet" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT NOT NULL, 
	part_of_parcellation_terminology TEXT NOT NULL, 
	ordinal INTEGER, 
	has_parent_parcellation_term_set TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(part_of_parcellation_terminology) REFERENCES "ParcellationTerminology" (id), 
	FOREIGN KEY(has_parent_parcellation_term_set) REFERENCES "ParcellationTermSet" (id)
);

CREATE TABLE "AnatomicalAnnotationSet" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT NOT NULL, 
	parameterizes TEXT NOT NULL, 
	revision_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(parameterizes) REFERENCES "AnatomicalSpace" (id), 
	FOREIGN KEY(revision_of) REFERENCES "ParcellationTerminology" (id)
);

CREATE TABLE "ParcellationTerm" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT NOT NULL, 
	symbol TEXT, 
	part_of_parcellation_term_set TEXT NOT NULL, 
	ordinal INTEGER, 
	has_parent_parcellation_term TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(part_of_parcellation_term_set) REFERENCES "ParcellationTermSet" (id), 
	FOREIGN KEY(has_parent_parcellation_term) REFERENCES "ParcellationTerm" (id)
);

CREATE TABLE "ParcellationAnnotation" (
	part_of_anatomical_annotation_set TEXT NOT NULL, 
	internal_identifier TEXT NOT NULL, 
	voxel_count INTEGER, 
	PRIMARY KEY (part_of_anatomical_annotation_set, internal_identifier, voxel_count), 
	FOREIGN KEY(part_of_anatomical_annotation_set) REFERENCES "AnatomicalAnnotationSet" (id)
);

CREATE TABLE "ParcellationAnnotationTermMap" (
	subject_parcellation_annotation TEXT NOT NULL, 
	subject_parcellation_term TEXT NOT NULL, 
	PRIMARY KEY (subject_parcellation_annotation, subject_parcellation_term), 
	FOREIGN KEY(subject_parcellation_term) REFERENCES "ParcellationTerm" (id)
);

CREATE TABLE "ParcellationAtlas" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT NOT NULL, 
	version TEXT NOT NULL, 
	has_anatomical_space TEXT NOT NULL, 
	has_anatomical_annotation_set TEXT NOT NULL, 
	has_parcellation_terminology TEXT NOT NULL, 
	specialization_of TEXT, 
	revision_of TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_anatomical_space) REFERENCES "AnatomicalSpace" (id), 
	FOREIGN KEY(has_anatomical_annotation_set) REFERENCES "AnatomicalAnnotationSet" (id), 
	FOREIGN KEY(has_parcellation_terminology) REFERENCES "ParcellationTerminology" (id), 
	FOREIGN KEY(specialization_of) REFERENCES "ParcellationAtlas" (id), 
	FOREIGN KEY(revision_of) REFERENCES "AnatomicalSpace" (id)
);

CREATE TABLE "ParcellationColorAssignment" (
	part_of_parcellation_color_scheme TEXT NOT NULL, 
	subject_parcellation_term TEXT NOT NULL, 
	color TEXT, 
	PRIMARY KEY (part_of_parcellation_color_scheme, subject_parcellation_term, color), 
	FOREIGN KEY(part_of_parcellation_color_scheme) REFERENCES "ParcellationColorScheme" (id), 
	FOREIGN KEY(subject_parcellation_term) REFERENCES "ParcellationTerm" (id)
);
