```
//ENTITY CONVOCATORIA
package com.persona.Backend.Entity.Operational.GestionHorario;



import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name="convocatoria")
public class Convocatoria extends BaseEntity {

	@Column(name = "codigo", length = 40, nullable = false)
	private String codigo;

	@Column(name = "anio",  nullable = false)
	private int anio;
	
	@Column(name = "trimestre",  nullable = false)
	private String trimestre;

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public int getAnio() {
		return anio;
	}

	public void setAnio(int anio) {
		this.anio = anio;
	}

	public String getTrimestre() {
		return trimestre;
	}

	public void setTrimestre(String trimestre) {
		this.trimestre = trimestre;
	}
}
//IREPOSITORY CONVOCATORIA
package com.persona.Backend.IRepository.Operational.GestionHorario;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionHorario.Convocatoria;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IConvocatoriaRepository extends IBaseRepository<Convocatoria, Long>{

}
//ISERVICE CONVOCATORIA
package com.persona.Backend.IService.Operational.GestionHorario;

import com.persona.Backend.Entity.Operational.GestionHorario.Convocatoria;
import com.persona.Backend.IService.IBaseService;

public interface IConvocatoriaService extends IBaseService<Convocatoria>{

}
//SERVICE CONVOCATORIA
package com.persona.Backend.Service.Operational.GestionHorario;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionHorario.Convocatoria;
import com.persona.Backend.IService.Operational.GestionHorario.IConvocatoriaService;
import com.persona.Backend.Service.BaseService;

@Service
public class ConvocatoriaService extends BaseService<Convocatoria> implements IConvocatoriaService {

}
//CONTROLLER CONVOCATORIA
package com.persona.Backend.Controller.Operational.GestionHorario;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionHorario.Convocatoria;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_horario/convocatoria")
public class ConvocatoriaController extends BaseController<Convocatoria> {

}

```