
def trigonometry(angle_deg):
    angle_rad = np.deg2rad(angle_deg)
    return {
        'rad': np.deg2rad(angle_deg),
        'sin': np.sin(angle_rad),
        'cos': np.cos(angle_rad),
        'tan': np.tan(angle_rad) if angle_deg != 180 else np.inf,
        'ctg': 1/np.tan(angle_rad) if angle_deg not in (90, 0) else np.inf,
    }
