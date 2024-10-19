from .app import db  # Importação relativa dentro do pacote

class ExperimentData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    page_variant = db.Column(db.String(10), nullable=False)
    impressions = db.Column(db.Integer, nullable=False)
    clicks = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<ExperimentData {self.page_variant} at {self.timestamp}>'
