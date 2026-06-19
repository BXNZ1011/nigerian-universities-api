-- Create table for Nigerian universities
CREATE TABLE universities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    slug VARCHAR(50),
    type VARCHAR(20),
    location VARCHAR(50),
    website VARCHAR(150),
    established INT
);

-- Insert sample data
INSERT INTO universities (name, slug, type, location, website, established) VALUES
('University of Lagos', 'unilag', 'Federal', 'Lagos State', 'https://unilag.edu.ng', 1962),
('Ahmadu Bello University', 'abu-zaria', 'Federal', 'Kaduna State', 'https://abu.edu.ng', 1962),
('Covenant University', 'covenant-university', 'Private', 'Ogun State', 'https://covenantuniversity.edu.ng', 2002);
